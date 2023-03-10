# Generated by Django 4.1 on 2022-12-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images/drinks')),
                ('category', models.ManyToManyField(related_name='drinks', to='home.category')),
            ],
        ),
    ]
