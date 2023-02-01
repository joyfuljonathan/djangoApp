from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Category2(models.Model):
    
    main_category = models.ForeignKey(Category, default =1, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(null = True, blank = True, upload_to= "images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='uncategorized')
    snippet = models.CharField(max_length=255, default='Click link above to read...')
    body = RichTextField(blank = True, null = True)
    # body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class EditPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255, default='Click link above to read...')
    body = models.TextField()
    header_image = models.ImageField(null = True, blank = True, upload_to= "images/")


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(null = True, blank = True, upload_to= "images/")
    category = models.CharField(max_length=255, default='uncategorized')
    product_snippet = models.CharField(max_length=255, default='Click link above to read...')
    product_body = RichTextField(blank = True, null = True)
    # body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User, related_name='blog_posts')
    
    # def __str__(self):
    #     return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class ProductData(models.Model):
    product_model = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    general_name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='uncategorized')
    category2 = models.CharField(max_length=255)
    sub_categoryOne = models.CharField(max_length=255)
    sub_categoryTwo = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    imgURL1 = models.CharField(max_length=255, null = True, blank = True)
    imgURL2 = models.CharField(max_length=255, null = True, blank = True)
    imgURL3 = models.CharField(max_length=255, null = True, blank = True)
    short_description = RichTextField(blank = True, null = True)
    spec = RichTextField(blank = True, null = True)
    weight = models.IntegerField();
    size_one = models.IntegerField();
    size_one = models.IntegerField();
    size_one = models.IntegerField();
    price = models.IntegerField();
    shipping = models.IntegerField();
    stock = models.IntegerField();
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class HomeProductData(models.Model):
    product_model = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    general_name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='uncategorized')
    category2 = models.CharField(max_length=255)
    sub_categoryOne = models.CharField(max_length=255)
    sub_categoryTwo = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    imgURL1 = models.CharField(max_length=255, null = True, blank = True)
    imgURL2 = models.CharField(max_length=255, null = True, blank = True)
    imgURL3 = models.CharField(max_length=255, null = True, blank = True)
    short_description = RichTextField(blank = True, null = True)
    spec = RichTextField(blank = True, null = True)
    weight = models.IntegerField();
    size_one = models.IntegerField();
    size_one = models.IntegerField();
    size_one = models.IntegerField();
    price = models.IntegerField();
    shipping = models.IntegerField();
    stock = models.IntegerField();
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
        


