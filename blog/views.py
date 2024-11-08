from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm


def blog_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog-detail', post_id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/blog_detail.html', context)


