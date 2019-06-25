from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {}
    return render (request,'nionic_app/index.html', context=my_dict)
