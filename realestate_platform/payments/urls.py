from django.urls import path
from . import views

urlpatterns = [
    path("appointments/<int:appointment_id>/create-order/", views.create_order, name="payment_create_order"),
    path("verify/", views.verify_payment, name="payment_verify"),
    path("admin-dashboard/", views.admin_dashboard, name="payments_admin_dashboard"),
]
