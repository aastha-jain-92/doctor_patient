from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, doctor_dashboard, patient_dashboard, CustomLoginView

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/patient/', patient_dashboard, name='patient_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
