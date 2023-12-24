from django.shortcuts import render
from blog.models import post
from django.utils import timezone
# Create your views here.


def blog_view(request):
    posts = post.objects.filter(status=1, published_date__lte=timezone.now())

    # Update counted_views for each post
    for p in posts:
        p.counted_views += 1
        p.save()

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request):
    return render(request,'blog/blog-single.html')

