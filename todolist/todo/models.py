from django.db import models

# Create your models here.

class Todo(models.Model):
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title

    