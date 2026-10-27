from django.contrib import admin
from .models import Property, PropertyImage, SavedProperty


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "locality", "city", "listed_price", "predicted_price", "status", "created_at"]
    list_filter = ["category", "status", "city"]
    search_fields = ["title", "locality", "city"]
    inlines = [PropertyImageInline]


@admin.register(SavedProperty)
class SavedPropertyAdmin(admin.ModelAdmin):
    list_display = ["buyer", "property", "saved_at"]
    list_filter = ["saved_at"]
