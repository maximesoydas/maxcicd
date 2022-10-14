from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace='profile')),
    path('lettings/', include('lettings.urls', namespace='letting')),
]
