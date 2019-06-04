from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'home.html')

def contact(request):
    subject = request.POST.get('subject', '')
    name = request.POST.get('name', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        html_body = (
            "<h3>Mensaje desde EL-Electric.net</h3>"
            "<hr>"
            "<h2>" + name + " - " + from_email + "</h2>"
            "<h1>" + subject + "</h1>"
            "<hr>"
            "<p>" + message + "</p>"
        )
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                ['edos21@gmail.com', "edgarironman@gmail.com"], html_message=html_body
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/?send-mail')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')