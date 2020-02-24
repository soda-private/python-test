from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    return HttpResponse("Hello, Quesuke!!")

def listEnquete(request):
    enqList = Question.objects.all()
    context = {
        'enquete_list' : enqList,
    }
    return render(request, 'quesuke/index.html', context=context)


