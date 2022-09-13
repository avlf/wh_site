from django.urls import path

from . import views

app_name = 'wh_info'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('character/', views.CharacterView.as_view(), name='character'),

]
