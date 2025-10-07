from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=100)  
    price = models.IntegerField()            
    description = models.TextField()         
    thumbnail = models.URLField()            
    category = models.CharField(max_length=50)  
    is_featured = models.BooleanField(default=False)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class book(models.Model):
    id=models.UUIDField(primary_key=True, editable=False)
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class author(models.Model):
    bio=models.TextField()
    books=models.ManyToManyField(book, related_name='authors')
    user=models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name