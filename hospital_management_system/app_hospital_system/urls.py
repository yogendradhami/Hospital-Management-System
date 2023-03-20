from django.urls import path
from . import views
from .views import Footer_Page

urlpatterns = [
    # this  is the  urls for homepage and department page
    path('department/', views.Department_Index, name='department' ),
    path('', views.Home, name= 'home'),
    
    # this is the  urls for bookappointment page

    path('book-appointment/', views.Appointment_Index, name='book-appointment'),
    path('appointment-booking/', views.Book_Appointment, name='appointment-booking'),

    # this is the urls for doctor page
    path('doctor/add/', views.Add_Doctor, name='doc-add'),
    path('doctor-index/',  views.Doctor_index, name='doctor-index'),

    
    # this is url for contact us  and footer page

    path('contact-us/', views.Contact_Us, name='contact-us'),
    path('footer/', Footer_Page.as_view(),name='footer'),

    # this is the url for staff 
    path('staff-index/', views.Staff_Index, name='staff-index'),
    path('add-staff/', views.Staff_Add, name='add-staff'),

    # this is url for medicine
    path('drug-index/', views.Drug_Index, name='drug-index'),
    path('add-drug/', views.Drug_Add,name='add-drug'),

    # this is url for patients
    path('patient-index/', views.Patient_Index,name='patient-index'),
    path('patient-view/<int:id>/', views.Patient_view,name='patient-view'),
    path('patient-add/', views.Patient_Add,name='patient-add'),
    path('patient-delete/<int:id>/', views.Patient_delete,name='patient-delete'),
    path('patient-edit/<int:id>/', views.Patient_edit,name='patient-edit'),
    path('patient-update/', views.Patient_update,name='patient-update'),

    # this is url for pharmacy management
    path('pharmacy-index/', views.Index_pharmacy, name='pharmacy-index'),
    path('pharmacy-delete/<int:id>/',views.Pharmacy_delete, name='pharmacy-delete'),

    # this is url for service page
    path('service-index/', views.Index_Service, name='service-index'),

    # this is url for search
    path('search/', views.Search, name='search'),

]