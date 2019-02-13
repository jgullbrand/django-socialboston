from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post

class PostListView (LoginRequiredMixin, ListView):
	model = Post
	template_name = "socialhome/home.html"	
	ordering = ["-post_date"]
	paginate_by = 5

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ["title", "text", "tag"]	
	template_name = "socialhome/add_post.html"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ["title", "text", "tag"]	
	template_name = "socialhome/add_post.html"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)	

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False			

class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post	
	template_name = "socialhome/post_detail.html"

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post	
	template_name = "socialhome/post_delete.html"
	success_url = "/"

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
