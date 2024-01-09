from django import template
from blog.models import post
from django.utils import timezone

register = template.Library()


@register.inclusion_tag('website/index-blog-area.html')
def latestblogslider(arg=6):
    posts = post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}