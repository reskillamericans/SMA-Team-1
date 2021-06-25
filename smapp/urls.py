from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    data = {
        'Project': 'Social Media Application',
        'Team': '1',
    }
    print(data)
    return HttpResponse(json.dumps(data))