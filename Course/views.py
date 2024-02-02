from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'indexs.html')
    
def django(request):
    return render(request,'django.html')

def mern(request):
    return render(request,'mern.html')
    