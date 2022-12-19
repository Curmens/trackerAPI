from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    photoUrls = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags', blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name