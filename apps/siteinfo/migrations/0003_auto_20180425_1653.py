# Generated by Django 2.0.1 on 2018-04-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0002_auto_20180424_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteinfo',
            name='sections',
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter'),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
