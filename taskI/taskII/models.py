from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    appropriate = models.CharField(choices=[
        ('u-8', 'Under 8'),
        ('8to15', '8-15'),
        ('adults', 'Adults')
    ], null=True, max_length=20)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




