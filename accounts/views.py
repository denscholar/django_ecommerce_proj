from base64 import urlsafe_b64decode
from tokenize import generate_tokens
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
from django.urls import reverse
from django.conf import settings

from accounts.form import (
    CustomPasswordResetConfirmForm,
    CustomPasswordResetForm,
    RegistrationForm,
    LoginForm,
)
from accounts.models import CustomUser

# For signing email
from django.core.mail import (
    send_mail,
    EmailMultiAlternatives,
    BadHeaderError,
    EmailMessage,
)

# to generate token
from .utils import TokenGenerator, generate_token

# threading
import threading


# this makes the email delivery veery fast
class EmailThread(threading.Thread):
    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
            return render(request, "accounts/activatefail.html")

        if generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, "Account activated successfully")
            return redirect("accounts:login")
        return render(request, "accounts/activatefail.html")


def login_view(request):
    context = {}
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        print(login_form)
        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully")
                return redirect("store:products")
            else:
                messages.error(request, "Empty username or password")
        else:
            messages.error(request, "Invalid credentials.")
    login_form = LoginForm()
    context = {"login_form": login_form}
    return render(request, "accounts/login.html", context)


def register(request, *args, **kwargs):
    user = request.user
    registration_form = RegistrationForm()
    context = {
        "registration_form": registration_form,
    }

    if user.is_authenticated:
        # add  a flash message here and redirect user to the home screen
        return redirect("store:products")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email").lower()
            password = form.cleaned_data.get("password1")
            authenticate(request, email=email, password=password)
            messages.success(request, "Registration successful. Please login")
            return redirect("accounts:login")
        else:
            context["registration_form"] = form
    return render(request, "accounts/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("store:products")


def requestResetPassword(request):
    context = {}
    if request.method == "POST":
        reset_form = CustomPasswordResetForm(request.POST)
        if reset_form.is_valid():
            email = reset_form.cleaned_data["email"]
            try:
                user = CustomUser.objects.get(email=email)
                current_site = get_current_site(request)
                email_subject = "Reset your password"
                message = render_to_string(
                    "accounts/reset-user-password.html",
                    {
                        "user": user,
                        "domain": current_site,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": generate_token.make_token(user),
                    },
                )
                email_message = EmailMessage(
                    email_subject, message, settings.EMAIL_HOST_USER, [email]
                )
                EmailThread(email_message).start()
                messages.info(
                    request,
                    "An link has been sent to "
                    + email
                    + ". use it to reset your password.",
                )
                return redirect(reverse("accounts:request-reset-password-form"))
            except CustomUser.DoesNotExist:
                messages.error(
                    request, "The email address is not associated with any account."
                )
                return redirect(reverse("accounts:request-reset-password-form"))
    else:
        reset_form = CustomPasswordResetForm()
        context = {"reset_form": reset_form}
    return render(request, "accounts/request-reset-password-form.html", context)


def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        if request.method == "POST":
            confirm_form = CustomPasswordResetConfirmForm(request.POST)
            if confirm_form.is_valid():
                new_password = confirm_form.cleaned_data["new_password"]
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password has been reset.")
                return redirect("accounts:login")
        else:
            confirm_form = CustomPasswordResetConfirmForm()

        context = {"confirm_form": confirm_form}
        return render(request, "accounts/password_reset_confirm.html", context)
    else:
        messages.error(request, "The reset password link is invalid or has expired.")
        return render(request, "accounts/password-reset-fail.html")
