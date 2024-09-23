from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "api-v1"

urlpatterns = [
    path("registration/", views.RegistrationAPIView.as_view(), name="registration"),
    path(
        "change-password/",
        views.ChangePasswordAPIView.as_view(),
        name="change-password",
    ),
    path("profile/", views.ProfileAPIView.as_view(), name="profile"),
    path("activation/<str:token>/", views.ActivationView.as_view(), name="activation"),
    path(
        "activation-resend/",
        views.ActivationResendView.as_view(),
        name="activation-resend",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
]
