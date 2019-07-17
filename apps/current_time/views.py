from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    context = {

        "time": strftime("%I:%M %p", localtime()),
        "date": strftime("%Y-%m-%d", localtime())
    }
    return render(request,'current_time/index.html', context)
    