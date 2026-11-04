from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="chat_inbox"),
    path("<int:pk>/", views.thread, name="chat_thread"),
    path("<int:pk>/since/", views.messages_since, name="chat_messages_since"),
    path("property/<int:property_id>/", views.start_conversation, name="chat_start"),
    path("conversation/<int:conversation_id>/appointment/", views.request_appointment, name="appointment_request"),
    path("appointment/<int:pk>/<str:action>/", views.update_appointment, name="appointment_update"),
    path("metrics/", views.appointment_metrics, name="appointment_metrics"),
    # Chatbot & Notifications
    path("api/chatbot/", views.api_chatbot, name="api_chatbot"),
    path("api/notifications/", views.api_notifications, name="api_notifications"),
    path("advisor/", views.advisor_view, name="estate_advisor"),
]
