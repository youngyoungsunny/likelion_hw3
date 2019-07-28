from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    class Meta:
        ordering = ['-pub_date']
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete="cascade") # 1:N의 관계라는 뜻
    author = models.ForeignKey(User, on_delete="cascade", null=True, blank=True) #.... null=True, blan=True꼭넣어주기....
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.blog_id, self.pk])

    def get_delete_url(self):
        return reverse('comment_delete', args=[self.blog_id, self.pk])
        #return reverse('comment_delete', args=[self.blog_id, self.pk])


    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])