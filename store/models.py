from django.db import models
from gsheets import mixins
from uuid import uuid4


# Create your models here.
class Storing(mixins.SheetPullableMixin,models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Contactno = models.IntegerField()
    Message = models.CharField(max_length=200)
    Attachment = models.ImageField(upload_to='goglestore/', null=True, blank=True)

    def __str__(self):
        return f'{self.Name} {self.Email} // {self.Contactno} '