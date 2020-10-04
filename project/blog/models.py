from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
from django.utils.translation import ugettext as _ 
from django.urls import reverse

class Post(models.Model):
    objects = None
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60,verbose_name='عنوان التدوينة')
    content = models.TextField(max_length=6000,verbose_name='نص التدوينة')
    post_date = models.DateTimeField(auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.pk])
        
        

    class Meta:
        ordering = ('-post_date',)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')    

class Comment(models.Model):
    objects = None
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=6000,verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'علق {} علي {}' .format(self.created_by,self.post)

    class Meta:
        ordering = ('-comment_date',)
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')