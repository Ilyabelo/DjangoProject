from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def myself(request):
    return render(request, 'myself.html')

def projects(request):
    return render(request, 'projects.html')