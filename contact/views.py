from django.contrib.messages import success
from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
# Create your views here.

def contact_form(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Message.objects.create(
             name=name,
             email=email,
             subject=subject,
             message=message)

        succes =True
        message = 'Contact form sent successfully'
    else:
        succes = False
        message = 'Request method is not valid'

    context = {'success': succes, 'message': message}
    return JsonResponse(context)
def contact(request):
    return render(request, 'contact.html')
