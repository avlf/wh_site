from django.contrib import admin
from django.urls import path, include

app_name = 'wh_site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wh_info/', include('wh_info.urls')),


]
