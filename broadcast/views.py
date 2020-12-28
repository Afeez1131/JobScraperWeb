from django.shortcuts import render
from django.conf import settings           
from django.http import HttpResponse
from twilio.rest import Client
from jobapp.views import job_filter

# Create your views here.
def broadcast_sms(request):
	# message = job_filter()
	# message = 
	message_to_broadcast = job_filter()
	client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
		if recipient:
			client.messages.create(to=recipient,
								   from_=settings.TWILIO_NUMBER,
								   body=message_to_broadcast)
	return HttpResponse("messages sent!", 200)


