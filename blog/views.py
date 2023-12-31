from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def blog_view(request, cat_name=None, author_username=None):
    posts = post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')

    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    current_post = get_object_or_404(post, pk=pid, status=1, published_date__lte=timezone.now())

    # Get the next and previous posts based on the current post's creation date
    next_post = post.objects.filter(status=1, published_date__gt=current_post.published_date, ).order_by(
        'published_date').first()
    prev_post = post.objects.filter(status=1, published_date__lt=current_post.published_date).order_by(
        '-published_date').first()

    # Increment the counted_views for the current post
    current_post.counted_views += 1
    current_post.save()
    context = {'post': current_post,
               'next_post': next_post,
               'prev_post': prev_post,
               }

    return render(request, 'blog/blog-single.html', context)


def blog_category(request, cat_name):
    posts = post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = post.objects.filter(status=1)

    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
