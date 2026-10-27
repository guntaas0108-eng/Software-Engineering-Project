from django.contrib import admin
from .models import Appointment, AppointmentEvent, Conversation, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ("sender", "body", "created_at", "read_at")
    can_delete = False


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "buyer", "seller", "first_message_at", "updated_at")
    search_fields = ("property__title", "buyer__username", "seller__username")
    readonly_fields = ("created_at", "updated_at", "first_message_at")
    inlines = [MessageInline]


class AppointmentEventInline(admin.TabularInline):
    model = AppointmentEvent
    extra = 0
    readonly_fields = ("actor", "old_status", "new_status", "note", "created_at")
    can_delete = False


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "conversation", "requested_by", "scheduled_for", "status", "confirmed_at")
    list_filter = ("status", "scheduled_for")
    search_fields = ("conversation__property__title", "requested_by__username")
    readonly_fields = ("created_at", "updated_at", "confirmed_at")
    inlines = [AppointmentEventInline]
