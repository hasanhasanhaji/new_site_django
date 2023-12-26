from django.contrib import admin
from blog.models import post,Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date' # let us see our object in admin panel based on date
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date')
    empty_value_display = 'null'
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']


admin.site.register(Category)
admin.site.register(post, PostAdmin)