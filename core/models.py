from django.db import models
import datetime


PRIORITY_CHOICES = (
  (1, 'Low'),
  (2, 'Normal'),
  (3, 'High'),
)


class Todo(models.Model):
    title = models.CharField(max_length=250, unique=True)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    class Admin:
        pass
