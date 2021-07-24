from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import Users
import json
from django.conf import settings
from .emails import send_forgot_password_mail







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
    user = Users.objects.all()
    user = request.user

    context = {
    'user': user,
    }
    return render(request, 'smapp/user_detail.html', {'context':context})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate( username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'smapp/login.html')



    


def password_reset(request, token):
    context = {}

    try:
        profile_obj = Profile.objects.filter(forgot_password_token).first()

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

            user_obj = Users.objects.get(id = user_id)
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

            if not Users.objects.all(username=username).first():
                messages.success(request, 'No user found with this username')
                return redirect('/forgot-password/')


            user = Users.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj = profile.objects.get(user = user_obj)
            profile_obj.forgot_password_token = token
            profile_obj.save()
            send_forgot_password_mail(user, token)
            messages.success(request, 'An email has been sent')
            return redirect('/forgot-password/')

            
    except:
        pass

    else:
        return render(request, 'forgot_password.html')

def send_forgot_password_mail(email, token):
    token = str(uuid.uuid4())
    email_from = EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def profile(request, user_id):
    user_obj = Users.objects.get(user = user_id)
    session_user = Users.objects.get(user = request.session['user'])
    session_following, create = Followers.objects.get_or_create(user = session_user)
    following, create = Followers.objects.get_or_create(user = session_user.id)
    check_user_followers = Followers.objects.filter(another_user = user_obj)

    is_followed = False
    if session_following.another_user.filter(name = user_name).exists() or following.another_user.filter(name = user_id).exists():
        is_followed = True
    else:
        is_followed = False
    param ={'user_obj':user_obj,'followers':check_user_followers, 'following':following,'is followed':is_followed}
    if 'usser' in request.session:
        return render(request, 'profile.html', param)

    else:
        return redirect('index')


def follow_user(request, user_id):
    other_user = Users.objects.get(user = user_id)
    session_user = request.session['user']
    get_user = Users.objects.get(name = session_user)
    check_follower = Followers.objects.get(user = get_user.id)
    is_followed = False
    if other_user.name != session_user:
        if check_follower.another_user.filter(name = other_user).exists():
            add_user = Followers.objects.get(user = get_user)
            add_user.another_user.remove(other_user)
            is_followed = False
            return redirect(f'/profile/{session_user}')
        else:
            add_user = Followers.objects.get(user = get_user)
            add_user.another_user.add(other_user)
            is_followed = True
            return redirect(f'/profile/{session_user}')

        return redirect(f'/profile/{session_user}')
    else:
        return redirect(f'profile/{session_user}')

