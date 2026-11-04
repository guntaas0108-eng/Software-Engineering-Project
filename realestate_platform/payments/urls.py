from django.urls import path
from . import views

urlpatterns = [
    path("checkout/property/<int:property_id>/", views.checkout_property, name="payment_checkout_property"),
    path("checkout/appointment/<int:appointment_id>/", views.checkout_appointment, name="payment_checkout_appointment"),
    path("process/", views.process_payment, name="payment_process"),
    path("receipt/<uuid:public_id>/", views.payment_receipt, name="payment_receipt"),
    path("my-transactions/", views.my_transactions, name="my_transactions"),
    path("appointments/<int:appointment_id>/create-order/", views.create_order, name="payment_create_order"),
    path("verify/", views.verify_payment, name="payment_verify"),
    path("admin-dashboard/", views.admin_dashboard, name="payments_admin_dashboard"),
]
