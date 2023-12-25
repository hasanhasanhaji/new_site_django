from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone
# Create your views here.


def blog_view(request):
    posts = post.objects.filter(status=1, published_date__lte=timezone.now())

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    pos = get_object_or_404(post, pk=pid)
    context = {'post': pos}
    return render(request, 'blog/blog-single.html', context)

