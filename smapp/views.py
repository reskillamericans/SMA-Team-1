from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import RegisterForm
from .models import Users
import json

# Create your views here.
def index(request):
    return render(request, 'smapp/index.html')

def register(request):
    form = RegisterForm
    # If this is a POST reqeust, we need to process form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = RegisterForm()
    # If a GET create a blank form 
    else:
        form = RegisterForm()
    
    return render(request, 'smapp/register.html', {'form':form})

def user_detail(request):
    # try:
    #     user = Users.objects.get(pk=id)
    # except Users.DoesNotExist:
    #     raise Http404('User does not exist')

    context = {
    'username': Users.username,
    'first_name': Users.first_name,
    'last_name': Users.last_name,
    'email': Users.email
    }
    return render(request, 'smapp/user_detail.html', context=context)

