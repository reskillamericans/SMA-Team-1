from django.shortcuts import render, get_object_or_404
from .models import Posts
from .forms import PostForm

def index(request):
    return render(request, 'smapp/index.html')

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit = False)
        post.author = request.user
        post.save()
    else:
        form = PostForm()
    return render(request, 'smapp/create_post.html', {'form':form})

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
