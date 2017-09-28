from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, AnswerForm

def post_list(request):
    posts = Post.objects.filter(is_question=True).order_by('-timestamp')
    return render(request, 'forum/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = timezone.now()
            post.is_question = True
            post.level = 0
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = timezone.now()
            post.is_question = True
            post.level = 0
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_edit.html', {'form': form})

def add_answer_to_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = timezone.now()
            post.parent_id = Post.objects.get(pk=pk)
            post.level = posts.level + 1
            post.save()
            return redirect('post_detail', pk=post.parent_id)
    else:
        form = AnswerForm()
    return render(request, 'forum/add_answer_to_post.html', {'form': form})
