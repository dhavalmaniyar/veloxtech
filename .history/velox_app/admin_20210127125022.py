from django.contrib import admin
from .models import CareersOpportunity,Applicant
# Register your models here.
admin.register(CareersOpportunity,Applicant)(admin.ModelAdmin)