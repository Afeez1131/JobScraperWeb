from django.core.management.base import BaseCommand
from django.utils import timezone
import string
import requests
from bs4 import BeautifulSoup
import re
from jobapp.models import JobModel

class Command(BaseCommand):
    help = 'Get new jobs'

    def handle(self, *args, **kwargs):


        url = 'https://www.myjobmag.com/'
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        job_sec = soup.find('ul', class_='job-list')
        li_job = job_sec.find_all('li', class_='job-list-li')

        for job in li_job:
            if 'mag-b' not in str(job):
                continue
            else:
                info = (job.find('li', class_='mag-b')).find('a')
                job_url = (job.find('li', class_='mag-b')).find('a').attrs['href']
                desc = job.find('li', class_='job-desc')
                date = job.find('li', id='job-date')
                field = job.find('li', id='job-field')

                if info != None and desc != None and date != None and field != None:
                    header = info.text
                    job_url = 'https://myjobmag.com' + job_url
                    desc = desc.string.strip()
                    field = field.string
                    date = date.string

                    JobModel.objects.create(
                        title = header,
                        date = date,
                        description=desc,
                        field = field,
                        url = job_url)
                else:
                    continue


        self.stdout.write('Latest Data Fetched for JOBMAG')