from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    image = models.ImageField(upload_to='dog/images/', verbose_name='狗狗照片')
    title=models.CharField(max_length=100,verbose_name='狗狗品种')
    price = models.CharField(max_length=100,null=True, verbose_name='狗狗价格')
    description=models.CharField(max_length=250,verbose_name='狗狗简介')
    url=models.URLField(blank=True,verbose_name='狗狗资源')

    class Meta:
        verbose_name='狗狗'
        verbose_name_plural = '狗狗'

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='dog_reviews')
    cat=models.ForeignKey(Dog,on_delete=models.CASCADE,related_name='dog_reviews')
    watchAgain=models.BooleanField()
    def __str__(self):
        return self.text