from django.shortcuts import render
import datetime as dt 

# Create your views here.
def index(request):
    return render(request,'movies/index.html')