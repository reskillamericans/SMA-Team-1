from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse
from .models import Users, Followers
from django.conf import settings


def index(request):
    return render(request, 'smapp/index.html')


def profile(request, user_id):
    user_obj = User.Objects.get(name=user_id)
    session_user = User.objects.get(name=request.session['user'])
    session_following, create = Followers.objects.get_or_create(user=session_user)
    following, create = Followers.objects.get_or_create(user=session_user.id)
    check_user_followers = Followers.objects.filter(another_user=user_obj)

    is_followed = False
    if session_following.another_user.filter(name=user_id).exists() or following.another_user.filter(name=user_id).exists():
        is_followed = True
    else:
        is_followed=False
    param = {'user_obj': user_obj,'followers':check_user_followers,'following': following,'is_followed':is_followed}
    if 'user' in request.session:
        return render(request, 'profile.html',param)
    else:
        return redirect('index')



def follow_user(request, user_id):
    other_user = User.Objects.get(name=user_name)
    session_user = request.session['user']
    get_user = User.objects.get(name=session_user)
    check_follower = Follwers.objects.get(user=get_user.id)
    is_followed = False
    if other_user.name != session_user:
        if check_follower.another_user.filter(name=other_user).exists():
            add_user = Followers.objects.get(user=get_user)
            add_user.another_user.remove(other_user)
            is_followed = False
            return redirect(f'/profile/{session_user}')
        else:
            add_user = Follwers.objects.get(user=get_user)
            add.user.another_user.add(other_user)
            is_followed = True
            return redirect(f'/profile/{session_user}')

        return redirect(f'/profile/{session_user}')

    else:
        return redirect(f'/profile/{session_user}')

