from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class LogoutTests(TestCase):
    """
    Regression test for: clicking Logout raised a 405. Django 5+'s
    LogoutView only accepts POST (GET-based logout is a CSRF risk — any
    page could embed <img src="/logout/">), but the nav bar used a plain
    GET <a href> link. Fixed by making it a POST form in templates/base.html.
    """

    def setUp(self):
        self.user = User.objects.create_user(username="logoutuser", password="testpass123")

    def test_get_logout_is_correctly_rejected(self):
        self.client.login(username="logoutuser", password="testpass123")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 405)

    def test_post_logout_succeeds_and_clears_session(self):
        self.client.login(username="logoutuser", password="testpass123")
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        protected = self.client.get(reverse("my_listings"))
        self.assertEqual(protected.status_code, 302)  # session really is gone

    def test_navbar_renders_logout_as_a_post_form_not_a_link(self):
        self.client.login(username="logoutuser", password="testpass123")
        response = self.client.get(reverse("property_list"))
        self.assertContains(response, f'action="{reverse("logout")}"')
        self.assertContains(response, 'method="post"')


class SignupTests(TestCase):
    def test_signup_creates_user_and_logs_in(self):
        response = self.client.post(reverse("signup"), {
            "username": "newuser",
            "password1": "a-very-strong-pass-1",
            "password2": "a-very-strong-pass-1",
        })
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertEqual(response.status_code, 302)
