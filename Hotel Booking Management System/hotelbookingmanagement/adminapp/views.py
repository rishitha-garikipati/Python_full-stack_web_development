from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def managementhomepage(request):
    return render(request,'managementhomepage.html')
def userhomepage(request):
    return render(request,'userhomepage.html')