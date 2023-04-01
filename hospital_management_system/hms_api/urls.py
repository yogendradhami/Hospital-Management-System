from django.urls import path
from .views import BookappointmetApiView, BookappointmentApiIdView

urlpatterns = [
    path('bookappointment/', BookappointmetApiView.as_view()),
    path('bookappointment/<int:id>/', BookappointmentApiIdView.as_view()),
]
