from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def digitalClock_app_index(request):
    return render(request,'digitalClock_app_templates/index.html')