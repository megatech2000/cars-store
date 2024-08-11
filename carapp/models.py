from django.db import models

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    image = models.ImageField(upload_to='media')
    desc = models.TextField()
    price = models.CharField(max_length=50, unique=True, null=True)
    hp = models.TextField()
    model = models.CharField(max_length=50, unique=True, null=True)
    mi = models.TextField()

    def __str__(self) -> str:
        return self.name
