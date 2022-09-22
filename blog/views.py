from django.http import HttpResponseRedirect
from django.views.generic import (TemplateView, ListView, DetailView,
     DeleteView, UpdateView, CreateView)
from django.urls import reverse_lazy, reverse
from blog.models import Comments, Gun
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView 
from blog.forms import CreateUser, CreateNewGun, Update
from django.shortcuts import render, get_object_or_404


class Index(TemplateView):
    template_name = 'base.html'

class GunsList(ListView):
    model = Gun
    context_object_name = 'guns_list'
    template_name = 'gunlist.html'

class GunsDetailView(DetailView):
    model = Gun
    context_object_name = 'gun_detail'
    template_name = 'gun_details.html'


class GunsCreate(CreateView):
    form_class = CreateNewGun
    template_name = 'guns_form.html'

    def get_queryset(self):
        return Gun._default_manager.all()
   
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse("GunBlog:guns_list")) 
  
  

class GunUpdate(UpdateView):
    model = Gun
    form_class = CreateNewGun
   

class GunDelete(DeleteView):
    model = Gun
    success_url = reverse_lazy("GunBlog:guns_list")



class UserLogin(LoginView):
    model = User
    

class LogOut(LogoutView):
    model = User


class UserCreate(CreateView):
    form_class = CreateUser
    template_name = 'create.html'
    
    def form_valid(self, form_class):
        user = form_class.save(commit=False)
        user.set_password(form_class.cleaned_data['password'])
        user.save()
        return super().form_valid(form_class)

    def get_success_url(self):
        return reverse("GunBlog:login")

class WrongPassword(TemplateView):
    template_name = 'wrong_password.html'


class CommentCreate(CreateView):
    form_class = Update
    model = Comments

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.comment_author = self.request.user
        obj.gun_comment = get_object_or_404(Gun, slug = self.kwargs['slug'])
        return super().form_valid(form)

    
    def get_success_url(self):
        return reverse("GunBlog:gun_details", kwargs={'slug':self.kwargs['slug']})
