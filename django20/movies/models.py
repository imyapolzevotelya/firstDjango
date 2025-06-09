from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(default=5)
    notes = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    watched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"