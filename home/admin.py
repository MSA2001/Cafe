from django.contrib import admin
from .models import Category, Drink, About, Contact

# Register your models here.

admin.site.register(Category)
admin.site.register(Drink)
admin.site.register(About)
admin.site.register(Contact)