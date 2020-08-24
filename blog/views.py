from django.shortcuts import render, get_object_or_404

from .models import Blog


def allblogs(request):
    blog = Blog.objects.all
    context = {
        "blog": blog,
    }
    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        "blog": blog,
    }
    return render(request, 'blog/detail.html', context)

