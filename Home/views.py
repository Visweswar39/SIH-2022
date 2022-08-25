from django.shortcuts import render, HttpResponse
from Home.myMod import HeyClass

obj = HeyClass()


# from joblib import load
# obj = load('.\model-build/job/savedModels/HeyClass.joblib')

def home(request):
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'jobs.html', {"result" : obj.fun()})

def admissions(request):
    return render(request, 'admissions.html')