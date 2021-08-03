import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Password_Resets


User = get_user_model()


def register(request):
    # register function needs to be implemented. Follow logiin method
    return render(request, 'accounts/register.html')


def login(request):
    
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.info(request, 'Invalid Credentials')
            return redirect('accounts:login')

        auth.login(request, user)
        return redirect('index')

    return render(request, 'accounts/login.html')


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

def user_detail(request):
    return render(request, 'user_detail.html')