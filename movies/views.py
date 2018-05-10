from django.shortcuts import render
import datetime as dt 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'movies/index.html')

@login_required(login_url='/accounts/login/')
def movie_list(request):
    return render(request, 'movies/movies.html')
