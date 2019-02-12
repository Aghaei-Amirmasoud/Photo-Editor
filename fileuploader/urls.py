from django.urls import path
from shalgham import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/editor', views.upload, name='upload'),
    path('upload/editor/gray/', views.gray, name='gray'),
    path('upload/editor/crop/', views.crop, name='crop'),
    path('upload/editor/resize/', views.resize, name='resize'),
    path('upload/editor/rotate/', views.rotate, name='rotate'),
    path('upload/editor/remove/', views.remove, name='remove'),
    path('upload/editor/share/', views.share, name='share'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.SHARE_URL, document_root=settings.SHARE_ROOT)
