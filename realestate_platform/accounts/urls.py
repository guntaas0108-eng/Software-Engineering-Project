from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Sovereign Administrator Command Center Routes
    path("command-center/", views.platform_admin_dashboard, name="platform_admin"),
    path("command-center/duplicate/<int:pk>/<str:action>/", views.admin_resolve_duplicate, name="admin_resolve_duplicate"),
    path("command-center/escrow/<int:pk>/<str:action>/", views.admin_moderate_payment, name="admin_moderate_payment"),
    path("command-center/user/<int:user_id>/verify/", views.admin_toggle_verification, name="admin_toggle_verification"),
    path("command-center/user/<int:user_id>/toggle-status/", views.admin_toggle_user_status, name="admin_toggle_user_status"),
    path("command-center/property/<int:pk>/toggle-status/", views.admin_toggle_property_status, name="admin_toggle_property_status"),
    path("command-center/diagnostics/run/", views.admin_run_diagnostics, name="admin_run_diagnostics"),
]
