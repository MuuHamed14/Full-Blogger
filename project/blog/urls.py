from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
   path('home/',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('post_detail/<int:id>/',views.post_detail,name='post_detail'),
   path('new_post/',views.PostCreateView.as_view(),name='new_post'),
   path('post_detail/<slug:pk>/post_update/',views.PostUpdateView.as_view(),name='post_update'),
   path('post_detail/<slug:pk>/post_delete/',views.PostDeleteView.as_view(),name='post_delete'),
]
