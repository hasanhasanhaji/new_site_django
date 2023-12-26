from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone
# Create your views here.


def blog_view(request):
    posts = post.objects.filter(status=1, published_date__lte=timezone.now())

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    current_post = get_object_or_404(post, pk=pid, status=1, published_date__lte=timezone.now())

    # Get the next and previous posts based on the current post's creation date
    next_post = post.objects.filter(status=1, published_date__gt=current_post.published_date,).order_by('published_date').first()
    prev_post = post.objects.filter(status=1, published_date__lt=current_post.published_date).order_by('-published_date').first()

    # Increment the counted_views for the current post
    current_post.counted_views += 1
    current_post.save()
    context = {'post': current_post,
               'next_post': next_post,
               'prev_post': prev_post,
               }


    return render(request, 'blog/blog-single.html', context)

