from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView

from .models import Appointment


class RegisterView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class DashboardView(TemplateView):
    template_name = "appointments/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appointments"] = Appointment.objects.all()
        return context


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ["client", "barber_name", "service_type", "date", "timeslot"]
    template_name = "appointments/book.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        barber_name = form.cleaned_data["barber_name"]
        date = form.cleaned_data["date"]
        timeslot = form.cleaned_data["timeslot"]
        if Appointment.objects.filter(barber_name=barber_name, date=date, timeslot=timeslot).exists():
            form.add_error(None, "This slot is already booked for the selected barber.")
            return self.form_invalid(form)
        return super().form_valid(form)
