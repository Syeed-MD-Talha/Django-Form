from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateProfileView.as_view(),name='profile'),
    path('list',views.ImageList.as_view(),name='profile_list')
]
