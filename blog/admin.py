from django.contrib import admin
from blog.models import post, Category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'  # let us see our object in admin panel based on date
    list_display = ('id', 'title', 'author', 'counted_views', 'status', 'published_date')
    empty_value_display = 'null'
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


admin.site.register(Category)
admin.site.register(post, PostAdmin)
