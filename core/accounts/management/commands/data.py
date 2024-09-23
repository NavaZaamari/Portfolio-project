from django.core.management.base import BaseCommand
from ...models import User, Profile
from blog.models import Post, Category
from faker import Faker
from datetime import datetime
import random


category_list = ["Technology", "Business", "Sports", "Entertainment", "Health"]


class Command(BaseCommand):
    help = "Create fake users"

    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(10):
            user = User.objects.create_user(email=faker.email(), password="nava123456")
            user.is_active = True
            user.is_verified = True
            user.save()
            profile = Profile.objects.get(user=user)
            profile.first_name = faker.first_name()
            profile.last_name = faker.last_name()
            profile.bio = faker.text(max_nb_chars=200)
            profile.save()

        for name in category_list:
            category = Category.objects.get_or_create(name=name)

        for _ in range(10):
            post = Post.objects.create(
                title=faker.text(max_nb_chars=10),
                content=faker.text(max_nb_chars=500),
                author=profile,
                category=Category.objects.get(name=random.choice(category_list)),
                status=True,
                created_date=datetime.now(),
            )
