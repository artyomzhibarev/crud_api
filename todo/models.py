from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    STATUS = (
        ('TODO', 'TODO'),
        ('INPROGRESS', 'INPROGRESS'),
        ('DONE', 'DONE'),
        ('CANCELED', 'CANCELED'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField(default='', blank=True)
    create_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='TODO')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
