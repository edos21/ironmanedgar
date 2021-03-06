from django.db import models
from django import forms
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext_lazy as _


class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', 0)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        if value and self.max_choices and len(value) > self.max_choices:
            raise forms.ValidationError('You must select a maximum of %s choice%s.'
                    % (str(self.max_choices), "s" if self.max_choices > 1 else ""))
        return value


class MultiSelectField(models.Field):
    __metaclass__ = models.TextField

    error_messages = {
        'invalid_choice': _(u'Value %r is not a valid choice.'),
        'null': _(u'This field cannot be null.'),
        'blank': _(u'This field cannot be blank.'),
    }

    def get_internal_type(self):
        return "CharField"

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def _get_FIELD_display(self, field):
        value = getattr(self, field.attname)
        choicedict = dict(field.choices)

    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name),
                    'help_text': self.help_text, 'choices': self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_db_prep_value(self, value, **kwargs):
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return ",".join(value)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        return value.split(",")

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            func = lambda self, fieldname = name, choicedict = dict(self.choices): ",".join([choicedict.get(value, value) for value in getattr(self, fieldname)])
            setattr(cls, 'get_%s_display' % self.name, func)

    def validate(self, value, model_instance):
        """
        Validates value and throws ValidationError. Subclasses should override
        this to provide validation logic.
        """
        try:
            from django.core import exceptions, validators
        except:
            return

        if not self.editable:
            # Skip validation for non-editable fields.
            return
        if self._check_choices and value:
            option_keys = [choice[0] for choice in self.choices]
            if isinstance(value, (list, tuple)):
                for option_value in value:
                    if option_value not in option_keys:
                        raise exceptions.ValidationError(self.error_messages['invalid_choice'] % option_value)
            else:
                return

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages['null'])

        if not self.blank and value in validators.EMPTY_VALUES:
            raise exceptions.ValidationError(self.error_messages['blank'])

