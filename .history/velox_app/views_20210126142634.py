from django.shortcuts import render,HttpResponse
from .models import CareersOpportunity
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def solution(request):
    return render(request,'solution.html')
def service(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def careers(request):
    careerData = CareersOpportunity.objects.all()
    return render(request,'careers.html',{'careerData':data})
