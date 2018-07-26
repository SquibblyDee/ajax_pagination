from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.core import serializers
import json

from .models import *

def index(request):
    return render(request, 'ajax_pagination_app/index.html', { "users": User.objects.all() })
# Create your views here.
def all_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')
def all_html(request):
    return render(request, 'ajax_pagination_app/all.html', { "users": User.objects.all() })
def find(request):
    return render(request, 'ajax_pagination_app/all.html',
        { "users":    User.objects.filter(first_name__startswith=request.POST['name']) }
    )