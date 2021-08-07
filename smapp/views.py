from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Posts, Categories, Users, Followers
from .forms import PostForm

def index(request):
    return render(request, 'index.html')

def create_post(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please login")
        return redirect("login")
    if request.method == 'POST':
        try:
            post = Posts()
            post.user_id = request.user
            post_category_id = request.POST.get('category_id')
            post.category_id = get_category_id(post_category_id)
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            messages.success(request, "Your post has been successfully created")
        except BaseException as e:
            messages.error(request, type(e).__name__)
            messages.error(request, e)
    if not request.POST.get('title') and request.POST.get('content'):
        context = {'error': 'The post was not successfully created. Please enter a title and content'}
        return render(request, 'create_post.html', context)
    return render(request, "create_post.html")


def get_category_id(category):
    if category == '':
        return None
    # If category exists, return category
    try:
        post_category = Categories.objects.get(cat_type=category)
        return post_category
    except Categories.DoesNotExist:
        # Else Create category
        new_category = Categories(cat_type=category)
        new_category.save()
        return new_category


def delete_post(request, id):
    if not request.user.is_authenticated:
        return redirect("index")
    post = Posts.objects.get(id=id)
    if request.user == post.user_id:
        Posts.objects.get(id=id).delete()
    return redirect('index')


def edit_post(request, id):
    if not request.user.is_authenticated:
        return redirect("index")

    try:
        post = get_object_or_404(Posts, id=id)
    except Posts.DoesNotExist:
        return redirect('index')

    if not request.user == post.user_id:
        return redirect('index')
    if request.method != 'POST':
        context = {'postobj': post,
                   'error': 'The post was not successfully updated. The title and content must be filled out.'}
        return render(request, "edit_post.html", context)
    post.category_id = get_category_id(request.POST.get('category'))
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    messages.success(request, "The post was successfully updated")
    context = {'postobj': post}

    return render(request, 'edit_post.html', context)




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
