from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.
from .models import Task


class PostListView(ListView):
    model = Task
    template_name = 'base/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Task
    template_name = 'base/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/post_create.html'
    # context_object_name = 'post'
    success_url = reverse_lazy('item_list')
    
class PostUpdateView(UpdateView):
    model = Task
    template_name = 'base/post_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('item_list')

class PostDeleteView(DeleteView):
    model = Task
    template_name = 'base/post_delete.html'
    success_url = reverse_lazy('item_list')
    context_object_name = 'post'