from django.contrib import admin
from .models import Book


# Register your models here.
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Book)
