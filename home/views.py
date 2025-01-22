from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def classes(request):
    return render(request, 'classes.html')

def my_account(request):
    return render(request, 'my_account.html') 
