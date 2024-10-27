from django.db import models
from django.utils import timezone


class Class(models.Model):
    
    address = models.CharField(max_length=50)
    class_number = models.PositiveIntegerField(default=1)
    class_time = models.CharField(max_length=10)
    class_created = models.DateTimeField(default=timezone.now)
    morabi = models.ForeignKey("User.User", on_delete=models.CASCADE)
    noe_tadris = models.BooleanField(default=False)

    
    def __str__(self):
        return self.class_number
    