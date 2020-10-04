from os import name
from django.urls import path
from .import views 

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile_update/',views.profile_update,name='profile_update'),
    # path('profile/<int:id>/', views.profile_detail, name='profile_detail'),

]
