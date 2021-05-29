from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username}'


class Note(models.Model):
    STATUS = (
        (0, 'TODO'),
        (1, 'INPROGRESS'),
        (2, 'DONE'),
        (3, 'CANCELED'),
    )

    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
