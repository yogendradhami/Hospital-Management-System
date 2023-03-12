from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.DepartmentIndex, name='department' ),
    path('logintem/', views.logintem, name= 'logintemp'),
    path('', views.Home, name= 'home'),
    path('book-appointment/', views.BookAppointment, name='book-appointment'),

]