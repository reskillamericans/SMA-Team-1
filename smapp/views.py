from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Posts, Categories
from .forms import PostForm

def index(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'auth.html')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please login")
        return redirect("auth")
    else:
        return render(request, 'dashboard.html')

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
            return redirect()
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
