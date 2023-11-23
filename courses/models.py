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


class Course(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
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
