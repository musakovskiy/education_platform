from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


def resize_image(instance, filename, size=(50, 50)):
    # Open the image file
    image = Image.open(instance.media_file.path)

    # Resize the image
    image.thumbnail(size)

    # Save the resized image back to the same path
    resized_filename = f"resized_{filename}"
    resized_path = f"media/resized/{resized_filename}"
    image.save(resized_path)

    # Return the path where the resized image should be stored
    return resized_path


class Course(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    media_file = models.ImageField(upload_to=resize_image, blank=True)

    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teaching = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["title"]
        verbose_name = "Курс"
        verbose_name_plural = "Курси"

    def __str__(self):
        return self.title


class User(AbstractUser):
    class Meta:
        ordering = ["username"]  # Додано сортування по імені користувача
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
