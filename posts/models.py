from django.db import models
from django.forms import DateTimeField
from cloudinary.models import CloudinaryField
# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'


    name = models.CharField(
        'Name', blank=False, null=False, max_length=15,
        db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )
    
    created_at = models.DateTimeField(
        'created DateTime', blank=True, auto_now_add=True
    )
    image = CloudinaryField('image', blank = True, null=True)
    like = models.IntegerField(null=True,blank=True, default=0)