from django.db import models

# Create your models here.

class CareersOpportunity(models.Model):
    opportunity = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    experience = models.CharField(max_length=40)
    isActive = models.BooleanField(default=True)
    skills = models.TextField()
    responsibilities = models.TextField()
    skills=models.IntegerField(null=True,blank=True)
    createdOn = models.DateField(default=timezone.now())

    def __str__(self):
        return self.opportunity