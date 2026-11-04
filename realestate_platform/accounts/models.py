from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    class Role(models.TextChoices):
        BUYER = "BUYER", "Accredited Buyer"
        SELLER = "SELLER", "Estate Proprietor / Seller"
        ADMIN = "ADMIN", "System Administrator"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.BUYER)
    phone = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        role = UserProfile.Role.BUYER
        if instance.is_staff or instance.is_superuser:
            role = UserProfile.Role.ADMIN
        elif instance.username.lower().startswith("seller"):
            role = UserProfile.Role.SELLER
        UserProfile.objects.create(user=instance, role=role)
    else:
        if hasattr(instance, "profile"):
            instance.profile.save()
