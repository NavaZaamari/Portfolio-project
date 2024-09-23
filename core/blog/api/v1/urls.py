from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"

router = DefaultRouter()

router.register("post", views.PostViewSet, basename="post")
router.register("category", views.CategoryViewSet, basename="category")
urlpatterns = router.urls
