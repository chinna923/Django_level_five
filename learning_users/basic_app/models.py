from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    portfoilo_site= models.URLField(blank=True)
    profile_pic= models.ImageField(upload_to= 'profile_pics', blank=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.profile_pic))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.user.username

