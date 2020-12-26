from django.core.management.base import BaseCommand
from django.utils import timezone
import string
import requests
from bs4 import BeautifulSoup
import re
from jobapp.models import JobModel

class Command(BaseCommand):
    help = 'Get new jobs from Jobzilla'


    def handle(self, *args, **kwargs):

        url = 'https://www.jobzilla.ng/jobs'
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        job_elem = soup.find('div', class_='container')
        article_job = job_elem.find_all('article', class_='card')

        for job in article_job:
            if 'footer' not in str(job):
                continue
            else:
                job_url = (job.find('h2')).find('a').attrs['href']
                job_name = job.find('h2')
                job_desc = job.find('footer')
                date = job.find('small')

                job_url = 'https://www.jobzilla.ng' + job_url
                title = job_name.text
                desc = job_desc.text.strip()
                description = re.sub(r'\s{2,4}', '', desc)
                date= date.string.strip()

                page = requests.get(job_url)
                soup = BeautifulSoup(page.content, 'html.parser')
                job_elem = soup.find('div', class_='container')
                field_list = (job_elem.find('small')).find_all('a', href=True)
                field = field_list[1].string

                JobModel.objects.create(
                    title = title,
                    date = date,
                    description=description,
                    field=field,
                    url = job_url)

        self.stdout.write('Latest Data Fetched for JobZilla')