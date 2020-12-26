from django.core.management.base import BaseCommand
from django.utils import timezone
import string
import requests
from bs4 import BeautifulSoup
import re
from . import jobberman, jobzilla, jobmag
from jobapp.models import JobModel

JobModel.objects.all().delete()
class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		

		jobmag.jobmag()
		jobzilla.jobzilla()
		# jobberman.jobberman()

		self.stdout.write('Latest Data Fetched')