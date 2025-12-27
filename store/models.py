from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#User Profile Model for book store called Readify
class UserProfile(models.Model): 
    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
    ('Prefer not to say', 'Prefer not to say')

]
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='profile'
)
    
    gender = models.CharField(
        max_length=30,
        choices=GENDER_CHOICES,
        blank=True
    )

    full_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null= True)
    
    instagram_link = models.URLField(max_length=500, blank=True)
    discord_link = models.URLField(max_length=500, blank=True)


    bio = models.TextField(blank=True)


    def __str__(self):
        return f"{self.user.username} Profile"





# -------------------------------------Book Model Start-------------------------------------



class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)

    # Optional: link author to a user account
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='author_profile'
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    FORMAT_CHOICES = [
        ('PDF', 'PDF'),
        ('EPUB', 'EPUB'),
        ('AUDIO', 'Audio Book'),
        ('PHYSICAL', 'Physical'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    authors = models.ManyToManyField(
        Author,
        related_name='books'
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='uploaded_books'
    )

    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)

    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)

    published_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    score = models.PositiveSmallIntegerField()  # 1–5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'user')


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')



# -------------------------------------Book Model End-------------------------------------


