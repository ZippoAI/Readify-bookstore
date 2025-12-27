from django.contrib import admin

# Register your models here.

from . models import UserProfile, UserLibrary, Review, Rating, Book, Author


admin.site.register(UserProfile)
admin.site.register(UserLibrary)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Book)
admin.site.register(Author)