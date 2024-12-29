from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Tag(models.Model):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=100)    


        
    def __str__(self):
        return self.name  
        
        

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=100)    

 


    def __str__(self):
        return self.name
          



class Page(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=100)   

    is_published = models.BooleanField(default=False)
    content = models.TextField()  




    def __str__(self):
        return self.title
    

class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')



class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    objects = PostManager()    

    title  = models.CharField(max_length=65)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=100)  
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m', blank=True, default="")
    cover_in_post_content = models.BooleanField(default=True)  
    created_at = models.DateField(auto_now_add=True)     
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_created_by' )   
    updated_at = models.DateField(auto_now=True) 
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_updated_by' )  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)   
    tags = models.ManyToManyField(Tag, blank=True, default="")    


    def __str__(self):
        return self.title
