from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    model = Post, Category
    list_display = ["title", "author", "category", "status"]
    fields = ["title", "author", "category", "status"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
