from django.db import models
from datetime import datetime
from django.urls import reverse


class Todo(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_edit', kwargs={'pk': self.pk})
