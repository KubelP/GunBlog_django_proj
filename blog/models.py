from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Caliber(models.Model):
    gun_caliber = models.CharField(max_length=25)
    
    def __str__(self):
        return self.gun_caliber

class Gun(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    gun_name = models.CharField(max_length=40, unique=True)
    gun_num = models.CharField(max_length=40)
    gun_body = models.TextField()
    gun_pic = models.ImageField(null=True, blank=True)
    caliber = models.ForeignKey(Caliber, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=25, unique=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.gun_name

    def get_absolute_url(self):
        return reverse("GunBlog:gun_details", kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.gun_name)
        return super().save(*args, **kwargs)

class Comments(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    gun_comment = models.ForeignKey(Gun, related_name='comments', on_delete=models.CASCADE, default=1)
    comment = models.TextField(max_length=500, verbose_name='Komentarz')
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.gun_comment} added by {self.comment_author}'









