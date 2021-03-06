from django.contrib import admin
from django.urls import path

from CodeRunner.views import run_code,home_page
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('run_code/',run_code,name="run_code"),
    path('',home_page,name='home_page'),
    
    rl(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
