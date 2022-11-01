from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views, user_views

app_name = 'wh_info'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration',user_views.UserCreationView.as_view(), name='registration'),
    path('character_list/', views.IndexView1.as_view(), name='index1'),
    path('character/<int:pk>', views.CharacterView.as_view(), name='character'),
    path('weapon_list/', views.IndexView2.as_view(), name='index2'),
    path('weapon/<int:pk>', views.WeaponView.as_view(), name='weapon'),
    path('roster_list/', views.IndexView3.as_view(), name='index3'),
    path('roster/<int:pk>', views.RosterView.as_view(), name='roster'),
    path('strategems_list/', views.StrategemALLView.as_view(), name='strategems_list'),
    path('strategems/<int:pk>', views.StrategemView.as_view(), name='strategems'),
    path('deployment_map/<int:pk>', views.DeploymentMapView.as_view(), name='deployment_map'),
    path('', views.main_view, name='main'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
