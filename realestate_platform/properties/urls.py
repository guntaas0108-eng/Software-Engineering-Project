from django.urls import path
from . import views

urlpatterns = [
    path("", views.property_list, name="property_list"),
    path("submit/", views.submit_property, name="submit_property"),
    path("my-listings/", views.my_listings, name="my_listings"),
    path("saved/", views.buyer_dashboard, name="buyer_dashboard"),
    path("<int:pk>/", views.property_detail, name="property_detail"),
    path("<int:pk>/edit/", views.edit_property, name="edit_property"),
    path("<int:pk>/delete/", views.delete_property, name="delete_property"),
    path("<int:pk>/save/", views.toggle_save_property, name="toggle_save_property"),
]
