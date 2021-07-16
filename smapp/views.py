import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .emails import send_forgot_password_mail
from .forms import RegisterForm
from .models import Password_Resets

User = get_user_model()

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
            post = form.save(commit = False)
            post.save()
            form = RegisterForm()

            return HttpResponseRedirect('../login/')
    # If a GET create a blank form 
    else:
        form = RegisterForm()
    
    return render(request, 'smapp/register.html', {'form':form})

def user_detail(request):
    
    # Return QuerySet
    user = User.objects.all()
    user = request.user

    context = {
    'user': user,
    }
    return render(request, 'smapp/user_detail.html', {'context':context})

def login(request):
    return render(request, 'smapp/login.html')


def password_reset(request, token):
    context = {}

    try:
        profile_obj = Password_Resets.objects.filter(token).first()

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'/password-reset/{token}/')

            if new_password != confirm_password:
                messages.success(request, 'both passwords must be equal.')
                return redirect(f'/password-reset/{token}/')

            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login/')

        context = {'user_id' : profile_obj.user.id}

    except Exception as e:
        print(e)
    return render(request, 'password_reset.html')



import uuid
def forgot_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not User.objects.all(username=username).first():
                messages.success(request, 'No user found with this username')
                return redirect('/forgot-password/')


            user = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj = Password_Resets(user_id=user, token=token)
            profile_obj.save()
            send_forgot_password_mail(user, token)
            messages.success(request, 'An email has been sent')
            return redirect('/forgot-password/')

    except:
        pass

    else:
        return render(request, 'forgot_password.html')

def send_forgot_password_mail(email, token):
    subject = 'Your Forgot Password Link'
    message = f'Click on the link to reset your password http://127.0.0.1:8000/password-reset/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
