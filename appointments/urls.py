from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path("book/", views.AppointmentCreateView.as_view(), name="appointment_book"),
]
