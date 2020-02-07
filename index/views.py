from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(req, *args, **kwargs):
  return HttpResponse("<h1>Hello World</h1>")