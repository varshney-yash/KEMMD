from django.contrib import admin
from django.urls import path
from users.urls import user_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns+=user_url_patterns