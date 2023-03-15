from django.urls import path
from . import views
from .views import FooterPage

urlpatterns = [
    path('department/', views.DepartmentIndex, name='department' ),
    path('', views.Home, name= 'home'),
    
    path('book-appointment/', views.AppointmentIndex, name='book-appointment'),
    path('doctor/add/', views.AddDoctor, name='doc-add'),
    path('make-order/', views.MakeOrder, name='make-order'),
    path('appointment-booking/', views.BookAppointment, name='appointment-booking'),
    path('contact-us/', views.ContactUs, name='contact-us'),
    path('footer/', FooterPage.as_view(),name='footer'),
    path('staff-index/', views.StaffIndex, name='staff-index'),
    path('add-staff/', views.StaffAdd, name='add-staff'),
    path('drug-index/', views.DrugIndex, name='drug-index'),
    path('add-drug/', views.DrugAdd,name='add-drug'),

]