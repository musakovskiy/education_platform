from django import forms
from .models import Course, User
from django.contrib.auth.forms import UserCreationForm


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category']


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    def clean(self):
        cleaned_data = super().clean()
        # Додайте перевірки на ваш смак
        return cleaned_data