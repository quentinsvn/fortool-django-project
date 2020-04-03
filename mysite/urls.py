from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iprestrict/', include('iprestrict.urls', namespace='iprestrict')),
    path('', include('blog.urls')),
]
