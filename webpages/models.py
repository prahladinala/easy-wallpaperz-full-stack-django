from unicodedata import category
from django.db import models

# Create your models here.


class MyWallz(models.Model):
    category_choices = (
        ('Avengers', 'Avengers'),
        ('DC', 'DC'),
        ('Coder', 'Coder'),
        ('Hacker', 'Hacker'),
        ('Nature', 'Nature'),
        ('Heros', 'Heros'),
        ('Motivational', 'Motivational'),
        ('Sports', 'Sports'),
        ('Animals', 'Animals'),
        ('Fantasy', 'Fantasy'),
        ('Fiction', 'Fiction'),
        ('History', 'History'),
        ('Movies', 'Movies'),
        ('Music', 'Music'),
        ('Politics', 'Politics'),
    )
    for_what_choices = (
        ('Mobile', 'Mobile'),
        ('Desktop', 'Desktop'),
        ('Tablet', 'Tablet'),
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='wallpapers/')
    category = models.CharField(choices=category_choices, max_length=200)
    for_what = models.CharField(choices=for_what_choices, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title
