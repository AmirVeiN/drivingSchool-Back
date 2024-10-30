from django.db import models
from django.utils import timezone


class Class(models.Model):
    
    address = models.CharField(max_length=50)
    class_number = models.PositiveIntegerField(unique=True)
    class_time = models.CharField(max_length=10)
    class_created = models.DateTimeField(default=timezone.now)
    morabi = models.ForeignKey("User.User", on_delete=models.CASCADE)
    noe_tadris = models.BooleanField(default=False)
    people = models.ManyToManyField("User.User", related_name="classes")
    day = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.class_number}, {self.morabi} , {self.day}'
    