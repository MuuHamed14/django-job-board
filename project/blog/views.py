from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib import messages


def all_posts(request):
    all_post = Post.objects.filter(active=True)
    paginator = Paginator(all_post,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_posts.html', {'all_post': page_obj})


def one_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.created_by = request.user
            new_form.save()
            messages.success(request,'Post Created Successfully')
            return redirect('blog:all_posts')
        else:
            form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def edit_post(request,id):
    post = get_object_or_404(Post,id=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request,'Post Edited Successfully')
            return redirect('blog:all_posts')
        else:
            form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


