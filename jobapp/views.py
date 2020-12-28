from django.shortcuts import render
from .models import JobModel
from django.db.models import Q

# Create your views here.
def index(request):
	objects = JobModel.objects.all()
	return render(request, 'jobapp/index.html', {'objects': objects,})

def job_filter():
	search = JobModel.objects.all().filter(field__contains='Sales' or 'checkers')
	# for s in search:
	# 	print(s.title)
	# 	print(s.url)

	search_q = JobModel.objects.filter(Q(field__contains='IT and ') | Q(field__contains = 'Software') | Q(field__contains='creative and design') | Q(field__contains='engineering & technology'))
	#search through all the models objects i.e, JobModel and use Q to search for the object containing ***
	message = dict()
	message_list = list()
	for ch in search_q:
		message['title'] = (ch.title)
		message['url'] = (ch.url)
		message['date'] = (ch.date)
		message_list.append(message)
	print(message_list)
	return str(message_list)	# convert the listed dictionary into a string
job_filter()