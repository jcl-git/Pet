from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cat(models.Model):
    image = models.ImageField(upload_to='cat/images/', verbose_name='猫咪照片')
    title=models.CharField(max_length=100,verbose_name='猫咪品种')
    price = models.CharField(max_length=100,null=True, verbose_name='猫咪价格')
    description=models.CharField(max_length=250,verbose_name='猫咪简介')
    url=models.URLField(blank=True,verbose_name='猫猫资源')

    class Meta:
        verbose_name='猫咪'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cat=models.ForeignKey(Cat,on_delete=models.CASCADE)
    watchAgain=models.BooleanField()
    def __str__(self):
        return self.text