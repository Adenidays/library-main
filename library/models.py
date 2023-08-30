from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} - {self.surname}'
    

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    publication_year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre,blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    views = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title} - {self.rating}'
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('book_detail', args=(self.slug, ))
