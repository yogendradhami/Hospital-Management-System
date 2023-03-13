from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.DepartmentIndex, name='department' ),
    path('logintem/', views.logintem, name= 'logintemp'),
    path('', views.Home, name= 'home'),
    path('book-appointment/', views.AppointmentIndex, name='book-appointment'),
    path('doctor/add/', views.AddDoctor, name='doc-add'),
    path('make-order/', views.MakeOrder, name='make-order'),
    path('appointment-booking/', views.BookAppointment, name='appointment-booking'),

]