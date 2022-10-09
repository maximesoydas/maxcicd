from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace='profile')),
    path('lettings/', include('lettings.urls', namespace='letting')),
]
