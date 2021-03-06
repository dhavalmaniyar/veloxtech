from django.shortcuts import render,HttpResponse
from .models import CareersOpportunity,Applicant
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
    return render(request,'careers.html',{'data':careerData})
def form(request):
    return render(request,'form.html')

def submit(request):
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    remail=request.POST['email']
    rphone=request.POST['phone']
    rresume=request.FILES['resume']
    submitdata=Applicant(name=fname,lastName=lname,email=remail,phone=rphone,resume=rresume)
    submitdata.save()
    return render(request,'index.html',{'message':'Form submitted successfully'})

def comment_submit(request):
    rname=request.POST['name']
    rcomment=request.POST['comment']
    remail=request.POST['email']
    submitData=Comment(name=rname,comment=rcomment,email=remail)
    submitData.save()
    return render(request,'index.html',{'message':'Thank you'})

