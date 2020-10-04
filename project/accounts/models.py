from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return 'profile_pics/%s.%s' % (instance.id,extension)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload,default='user.png')
    
    def __str__(self):
        return '{} profile'.format(self.user.username)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

  
post_save.connect(create_profile,sender=User)
