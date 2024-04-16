from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Tillar(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    cart_img=models.ImageField(upload_to='tillar/',null=True,blank=True)
    def __str__(self):
        return self.name

class Kitob(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,)
    til=models.ForeignKey(Tillar,on_delete=models.CASCADE,null=True,blank=True,related_name='til')
    body=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to='kitob/',null=True,blank=True)
    create_date=models.DateTimeField(auto_now=True)
    update_date=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    place=models.ForeignKey(Kitob,on_delete=models.CASCADE,related_name='izohlar')
    comment_text=models.TextField()
    start_give=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    create_at=models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.start_give)
    
