from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if "publish" in request.POST:  # Если нажата кнопка "Опубликовать"
                post.is_published = True
            post.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})

@login_required
def publish_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.is_published = True
    post.save()
    return redirect("post_detail", post_id=post.id)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect("post_detail", post_id=post.id)

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_form": comment_form
    })

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})
