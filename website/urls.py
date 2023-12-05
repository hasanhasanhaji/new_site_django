from website.views import index_view, about_view, contact_view
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('url',view)
    path('', index_view),
    path('about/', about_view),
    path('contact/', contact_view)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
