from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="chat_inbox"),
    path("start/<int:property_id>/", views.start_conversation, name="chat_start"),
    path("<int:pk>/", views.thread, name="chat_thread"),
    path("<int:pk>/messages/", views.messages_since, name="chat_messages_since"),
    path("<int:conversation_id>/appointments/request/", views.request_appointment, name="appointment_request"),
    path("appointments/<int:pk>/<str:action>/", views.update_appointment, name="appointment_update"),
    path("metrics/appointments/", views.appointment_metrics, name="appointment_metrics"),
]
