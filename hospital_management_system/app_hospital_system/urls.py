from django.urls import path
from . import views
from .views import Footer_Page

urlpatterns = [
    path('department/', views.Department_Index, name='department' ),
    path('', views.Home, name= 'home'),
    
    path('book-appointment/', views.Appointment_Index, name='book-appointment'),
    path('doctor/add/', views.Add_Doctor, name='doc-add'),
    path('make-order/', views.Make_Order, name='make-order'),
    path('appointment-booking/', views.Book_Appointment, name='appointment-booking'),
    path('contact-us/', views.Contact_Us, name='contact-us'),
    path('footer/', Footer_Page.as_view(),name='footer'),
    path('staff-index/', views.Staff_Index, name='staff-index'),
    path('add-staff/', views.Staff_Add, name='add-staff'),
    path('drug-index/', views.Drug_Index, name='drug-index'),
    path('add-drug/', views.Drug_Add,name='add-drug'),

]