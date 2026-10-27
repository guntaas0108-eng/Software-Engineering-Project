from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    """
    Sprint 2 (Person 2): registration. Kept on Django's built-in User model
    for Sprint 1/2 — add a Profile model here later if buyer/seller needs
    diverge (e.g. a seller-only verification flag).
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("property_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
