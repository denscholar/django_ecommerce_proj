from django.urls import include, path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("products/", views.product, name="products"),
    path("profile/", views.profile, name="profile"),
]