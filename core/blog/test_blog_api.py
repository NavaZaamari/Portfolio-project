from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import Post, Category


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
class TestBlogAPI:

    def test_post_list(self, common_user):
        user, profile = common_user
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("http://127.0.0.1:8000/blog/api/v1/post/")
        assert response.status_code == 200

    def test_post_detail(self, common_user):
        user, profile = common_user
        client = APIClient()
        client.force_authenticate(user=user)
        post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=profile
        )
        post.status = True
        post.save()
        response = client.get(f"http://127.0.0.1:8000/blog/api/v1/post/{post.id}/")
        assert response.status_code == 200

    def test_post_delete(self, common_user):
        user, profile = common_user
        client = APIClient()
        client.force_authenticate(user=user)
        post = Post.objects.create(
            title="Test Post", content="This is a test post!", author=profile
        )
        post.status = True
        post.save()
        response = client.delete(f"http://127.0.0.1:8000/blog/api/v1/post/{post.id}/")
        assert response.status_code == 204

    def test_category_create(self, common_user):
        user, profile = common_user
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post(
            "http://127.0.0.1:8000/blog/api/v1/category/",
            {"name": "Products"},
            format="json",
        )
        assert response.status_code == 201
