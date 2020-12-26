from django.core.management.base import BaseCommand
from django.utils import timezone
import string
import requests
from bs4 import BeautifulSoup
import re
from jobapp.models import JobModel

class Command(BaseCommand):
    help = 'Get new jobs from Jobberman'


    def handle(self, *args, **kwargs):
        
        url = 'https://www.jobberman.com/jobs?page=1'
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(class_='search-main__content')

        job_elem = results.find_all('article', class_="search-result")

        JobModel.objects.all().delete()
        for job in job_elem:
            if 'group' not in str(job):
                job_title = ((job.find('header', class_='search-result__header')).find('h3')).text.strip()
                job_url = (job.find('header', class_='search-result__header')).find('a').attrs['href']
                job_time = (job.find(class_='if-wrapper-column align-self--end text--right')).text.strip()
                content = (job.find('div', class_='search-result__content transform-y-center content-hide--under-md')).text.strip()
                field = (job.find('div', class_='if-wrapper-row ellipses')).find('span', class_="padding-lr-10 gutter-flush-under-lg").text.strip()

                JobModel.objects.create(
                title = job_title,
                url =  job_url,
                description = content,
                field = field,
                date = job_time)
            else:
                pass
        self.stdout.write('Latest Data Fetched for Jobberman')