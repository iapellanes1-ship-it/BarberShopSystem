from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Appointment(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    barber_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    date = models.DateField()
    timeslot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("barber_name", "date", "timeslot")
        ordering = ["date", "timeslot", "barber_name"]

    def __str__(self):
        return f"{self.barber_name} — {self.service_type} on {self.date} at {self.timeslot}"
