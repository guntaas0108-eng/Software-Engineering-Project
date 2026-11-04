from .models import UserProfile


def user_role_context(request):
    """
    Universally injects user role, strict AI bot identity, and admin status
    into all templates so the UI cleanly segregates Buyer, Seller, and Admin interfaces.
    """
    user = request.user
    if not user.is_authenticated:
        return {
            "user_role": "GUEST",
            "is_buyer": True,
            "is_seller": False,
            "is_platform_admin": False,
            "bot_mode": "buyer",
            "bot_name": "Estate Concierge AI",
            "bot_role_label": "ACCREDITED BUYER",
            "bot_badge_color": "var(--gold-lt)",
        }

    is_admin = bool(
        user.is_staff
        or user.is_superuser
        or (hasattr(user, "profile") and user.profile.role == UserProfile.Role.ADMIN)
    )

    # Determine primary role
    if hasattr(user, "profile") and user.profile:
        role = user.profile.role
    else:
        role = UserProfile.Role.SELLER if user.username.lower().startswith("seller") else UserProfile.Role.BUYER

    is_seller = (role == UserProfile.Role.SELLER)
    is_buyer = (role == UserProfile.Role.BUYER)

    if is_seller:
        bot_mode = "seller"
        bot_name = "Portfolio Strategist AI"
        bot_role_label = "ESTATE PROPRIETOR"
        bot_badge_color = "#79D6A0"
    elif is_admin:
        bot_mode = "admin"
        bot_name = "Executive Platform AI"
        bot_role_label = "SOVEREIGN ADMINISTRATOR"
        bot_badge_color = "#F0D98A"
    else:
        bot_mode = "buyer"
        bot_name = "Estate Concierge AI"
        bot_role_label = "ACCREDITED BUYER"
        bot_badge_color = "var(--gold-lt)"

    return {
        "user_role": role,
        "is_buyer": is_buyer,
        "is_seller": is_seller,
        "is_platform_admin": is_admin,
        "bot_mode": bot_mode,
        "bot_name": bot_name,
        "bot_role_label": bot_role_label,
        "bot_badge_color": bot_badge_color,
    }
