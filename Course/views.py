from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'course_content.html')
    
def django(request):
    return render(request,'django.html')

def mern(request):
    return render(request,'mern.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def pricing(request):
    return render(request,'pricing.html')