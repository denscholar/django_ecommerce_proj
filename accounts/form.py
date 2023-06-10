from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import CustomUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label="first name", widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label="last name", widget=forms.TextInput()
    )
    email = forms.CharField(
        label="email", widget=forms.TextInput()
    )
    phone_number = forms.CharField(
        widget=forms.TextInput()
    )

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Phone number already exists")
        return phone_number
    
    
    
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ("email", "password")
        
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("Invalid login credentials")
        return self.cleaned_data
    
    
class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("This email address doesn't have an associated user account.")
        return email


class CustomPasswordResetConfirmForm(forms.Form):
    new_password = forms.CharField(
        label="New password", 
        widget=forms.PasswordInput(), 
        max_length=128, 
        min_length=8
    )
    confirm_password = forms.CharField(
        label="Confirm new password", 
        widget=forms.PasswordInput(), 
        max_length=128, 
        min_length=8
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")