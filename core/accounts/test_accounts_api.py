from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User, Profile


@pytest.fixture
def common_user(db):
    user = User.objects.create_user(
        email="navazaamaritest@gmail.com", password="nava123456"
    )
    user.is_verified = True
    user.is_active = True
    user.save()
    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={
            "first_name": "Nava",
            "last_name": "Zaamari",
            "bio": "A backend developer in training.",
            "image": "",
        },
    )
    return user, profile


@pytest.mark.django_db
class TestAccountsAPI:
    def test_registration(self):
        client = APIClient()
        data = {
            "email": "navaishere@example.com",
            "password": "nava123456",
            "password1": "nava123456",
        }
        response = client.post(
            "http://127.0.0.1:8000/accounts/api/v1/registration/", data
        )
        assert response.status_code == 201

    def test_profile_access(self, common_user):
        user, profile = common_user
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("http://127.0.0.1:8000/accounts/api/v1/profile/")
        assert response.status_code == 200
