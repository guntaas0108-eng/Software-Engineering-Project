from django import forms
from django.utils import timezone
from .models import Appointment, Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={
                "rows": 2, "placeholder": "Write a message…", "maxlength": 4000,
                "class": "form-control",
            })
        }

    def clean_body(self):
        body = self.cleaned_data["body"].strip()
        if not body:
            raise forms.ValidationError("Enter a message before sending.")
        return body


class AppointmentForm(forms.ModelForm):
    scheduled_for = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"},
            format="%Y-%m-%dT%H:%M",
        ),
    )

    class Meta:
        model = Appointment
        fields = ["scheduled_for", "note"]
        widgets = {
            "note": forms.TextInput(attrs={
                "maxlength": 500, "placeholder": "Optional note for the seller",
                "class": "form-control",
            })
        }

    def clean_scheduled_for(self):
        value = self.cleaned_data["scheduled_for"]
        if value <= timezone.now():
            raise forms.ValidationError("Choose a future date and time.")
        return value
