from django.urls import path

from . import views

app_name = 'wh_info'

urlpatterns = [
    path('character_list/', views.IndexView.as_view(), name='index1'),
    path('character/<int:pk>', views.CharacterView.as_view(), name='character'),
    path('weapon_list/', views.IndexView2.as_view(), name='index2'),
    path('weapon/<int:pk>', views.WeaponView.as_view(), name='weapon'),
    path('weapon_list/', views.IndexView3.as_view(), name='index3'),
    path('roster/<int:pk>', views.RosterView.as_view(), name='roster'),
    path('', views.main_view, name='main'),

]
