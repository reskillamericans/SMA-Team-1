from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Posts, Categories
from .forms import PostForm

def index(request):
    return render(request, 'index.html')

def create_post(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please login")
        return redirect("login")
    if not request.POST.get('title') and request.POST.get('content'):
        context = {'error': 'The post was not successfully created. Please enter a title and content'}
        return render(request, 'create_post.html', context)
    if request.method == 'POST':
        try:
            post = Posts()
            post.user_id = request.user
            post_category_id = request.POST.get('category_id')
            post.post_category_id = get_category_id(post_category_id)
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            messages.success(request, "Your post has been successfully created")
            return redirect('index')
        except BaseException as e:
            messages.error(request, type(e).__name__)
            messages.error(request, e)
            return render(redirect, 'index')

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

def edit_post(request, pk):
    post = get_object_or_404(Posts, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
        else:
            form = PostForm(instance = post)
    return(render, 'smapp/edit_post.html', {'form': form})

def delete_post(request, key):
    post = Posts.objects.get(pk=key)
    post.delete()
    return render(request, 'delete_post.html')
