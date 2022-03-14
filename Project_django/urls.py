
from django.contrib import admin
from django.urls import include, path

from hello.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('try/', index),
    path('__debug__/', include('debug_toolbar.urls')),
]
