from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='birds'),
    path('birds/<int:bird_id>', views.birds_details, name='details'),

    path('bird/create/', views.CreateBird.as_view(), name='bird_create'),

    path('bird/<int:pk>/update', views.UpdateBird.as_view(), name='bird_update'),

    path('bird/<int:pk>/delete', views.DeleteBird.as_view(), name='bird_delete'),
]
