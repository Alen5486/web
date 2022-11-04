from django.http import HttpResponse
from django.shortcuts import render
from.models import *


# Create your views here.
def index(requesst):
    context = {"title": "Rolls Royce"}
    Blogdata=Blog.objects.all()
    context = {"blogs":Blogdata}
   
    return render(requesst, "index.html", context=context)
    
