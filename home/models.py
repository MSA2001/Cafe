from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='drinks')
    detail = models.TextField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/drinks')

    def __str__(self):
        return f'{self.name}-{self.category}- {self.price}$'



