from django.urls import path
from . import views
from .views import Footer_Page

urlpatterns = [
    path('department/', views.Department_Index, name='department' ),
    path('', views.Home, name= 'home'),
    
    path('book-appointment/', views.Appointment_Index, name='book-appointment'),
    path('doctor/add/', views.Add_Doctor, name='doc-add'),
    
    path('appointment-booking/', views.Book_Appointment, name='appointment-booking'),
    path('contact-us/', views.Contact_Us, name='contact-us'),
    path('footer/', Footer_Page.as_view(),name='footer'),
    path('staff-index/', views.Staff_Index, name='staff-index'),
    path('add-staff/', views.Staff_Add, name='add-staff'),
    path('drug-index/', views.Drug_Index, name='drug-index'),
    path('add-drug/', views.Drug_Add,name='add-drug'),

    path('patient-index/', views.Patient_Index,name='patient-index'),
    path('patient-view/<int:id>/', views.Patient_view,name='patient-view'),
    path('patient-add/', views.Patient_Add,name='patient-add'),
    path('patient-delete/<int:id>/', views.Patient_delete,name='patient-delete'),
    path('patient-edit/<int:id>/', views.Patient_edit,name='patient-edit'),
    path('patient-update/', views.Patient_update,name='patient-update'),


    path('pharmacy-index/', views.Index_pharmacy, name='pharmacy-index'),
    path('service-index/', views.Index_Service, name='service-index'),
    path('doctor-index/',  views.Doctor_index, name='doctor-index'),
    

]