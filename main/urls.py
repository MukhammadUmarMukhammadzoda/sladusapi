from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),
                  path('create', views.create, name='create'),
                  path('update/<int:pk>/', views.update, name='update'),
                  path('delete/<int:pk>/', views.delete, name='delete')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)