# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_by_category, name='post_list'),
    path('category/<str:category>/', views.post_list_by_category, name='post_list_by_category'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('doctor/new/', views.doctor_create_post, name='doctor_create_post'),
    path('doctor/mine/', views.doctor_posts, name='doctor_posts'),
    path('patient/', views.patient_blogs, name='patient_blogs'),

]
