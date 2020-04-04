from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from mdeditor.fields import MDTextField

class profileModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    # contactNumber = models.IntegerField(blank = True, null=True)
    # canPOST = models.BooleanField(default =  False)
    writer = models.BooleanField(default =  False)
    regular_user = models.BooleanField(default =  True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


choices=(
    ('published','Published'),
('draft','draft')
)

from django.db import models

        
class Parent_Category(models.Model):
    Name      =       models.CharField(max_length=500)
    description      =       models.TextField(max_length=500)
    slug      =       models.CharField(max_length=500)
    image       =       models.ImageField(blank=True)
    public    =  models.BooleanField(default=True)
    Private   =       models.ManyToManyField(User,blank=True )
    Date        =       models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.slug
        
    class Meta:
        verbose_name_plural= 'Parent Categories'
        ordering = ['-Date']

class Category(models.Model):
    Name      =       models.CharField(max_length=500)
    slug      =       models.CharField(max_length=500)
    Parent_Category    =       models.ForeignKey(Parent_Category, on_delete=models.CASCADE,blank=True ,null=True)
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name_plural= 'Categories'

class Sub_Category(models.Model):
    Name      =       models.CharField(max_length=500)
    slug      =       models.CharField(max_length=500)
    Category    =       models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural= 'Subcategories'

class Article(models.Model):
    Parent_Category =   models.ForeignKey(Parent_Category, on_delete=models.CASCADE,blank=True ,null=True)
    catagory    =       models.ForeignKey(Category,on_delete=models.CASCADE)
    # sub_catagory=       models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    title       =       models.CharField(max_length=1000)
    slug        =       models.CharField(max_length=1000)
    slug1       =       models.CharField(max_length=1000)
    status      =       models.CharField(max_length=100,choices=choices)
    image       =       models.ImageField(blank=True)
    description =        MDTextField()
    Date        =       models.DateTimeField(auto_now=True)
    updated     =       models.DateTimeField(auto_now_add=True)
    search_vector = SearchVectorField(null=True,blank=True)

    class Meta(object):
        indexes = [GinIndex(fields=['search_vector'])]
        ordering = ["-Date","-updated"]

    def __str__(self):
            return self.title
    def get_absolute_url(self):
        return "/%s/" % self.slug






