from django.shortcuts import render
from .models import User,Blog,tlogComment,Comment

# Create your views here.
def user_page(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user.html', context=context)


def blog_page(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'blog.html', context=context)


def comment_page(request):
    comment = Comment.objects.all()
    context = {
        'comment': comment
    }
    return render(request, 'comment.html', context=context)


def tlogcomment_page(request):
    tlogcomment = tlogComment.objects.all()
    context = {
        'tlogcomment': tlogcomment
    }
    return render(request, 'tlogcomment.html', context=context)

