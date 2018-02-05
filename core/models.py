from django.db import models
import datetime


class Todo(models.Model):

    PRIORITY_CHOICES = (
      ('Baixa', 'Baixa'),
      ('Normal', 'Normal'),
      ('Alta', 'Alta'),
    )

    title = models.CharField(max_length=250, unique=True)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Normal')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']
