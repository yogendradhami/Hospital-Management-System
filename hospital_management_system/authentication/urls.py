from django.urls import path
from .views import LoginPage, RegisterPage, LogoutPage
from . import views

urlpatterns =[
    path('login/', LoginPage.as_view(), name='user_login'),
    path('logout/',LogoutPage.as_view(), name= 'logout'),
    path('register/', RegisterPage.as_view(), name='user_registration'),
    path('dashboard', views.Dashboard, name='dashboard' ),
    path('change-password/<token>/', views.ChangePassword, name='change-password'),
    path('forgot-password/', views.forgetPassword, name='forgot-password'),
]