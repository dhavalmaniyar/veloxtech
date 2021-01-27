from django.contrib import admin
from .models import CareersOpportunity,Applicant,Comment
# Register your models here.
admin.register(CareersOpportunity,Applicant,Comment)(admin.ModelAdmin)