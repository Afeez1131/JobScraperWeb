from django.contrib import admin
from .models import JobModel
# Register your models here.


@admin.register(JobModel)
class JobModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'url')
	search_fields = ('title', 'description', 'url')