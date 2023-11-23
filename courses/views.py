# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Course, User
from .forms import CourseForm


@login_required
def index(request):
    num_users = User.objects.count()

    num_courses = Course.objects.count()

    context = {
        'num_users': num_users,
        'num_courses': num_courses,
    }

    return render(request, 'courses/index.html', context=context)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'courses/category_list.html'
    paginate_by = 5


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('courses:category-list')


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('courses:category-list')


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy('courses:category-list')


class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    paginate_by = 5


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Course


class CourseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:course-list')


class CourseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:course-list')


class CourseDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Course
    success_url = reverse_lazy('courses:course-list')
