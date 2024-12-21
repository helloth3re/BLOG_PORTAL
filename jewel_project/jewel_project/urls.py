
from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HOME, name = 'home'),
    path('category/', views.CAT, name = 'category'),
    path('contact/', views.CONT, name = 'contact'),
    path('gallery/', views.GALL, name = 'gallery'),
    path('base/', views.BASE, name = 'base'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
