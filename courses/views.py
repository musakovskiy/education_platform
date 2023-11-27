# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Course, User
from .forms import CourseForm, UserCreateForm
from django.shortcuts import redirect
from django.contrib.auth import login


def index(request):
    num_users = User.objects.count()
    num_courses = Course.objects.count()

    # Fetch all categories from the database
    categories = Category.objects.all()

    context = {
        'num_users': num_users,
        'num_courses': num_courses,
        'categories': categories,  # Add this line to include categories in the context
    }

    return render(request, 'courses/index.html', context=context)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'courses/category_list.html'


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


class UserCreateView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        print("Form is valid")
        response = super().form_valid(form)
        login(self.request, self.object)  # Log in the user
        print("User logged in")
        return response


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Category
