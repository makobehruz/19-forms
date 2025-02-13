from django.db import models
from django.shortcuts import reverse


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('lessons:detail', args=[self.pk])

    def get_edit_url(self):
        return reverse('lessons:edit', args=[self.pk])

    def get_delete_url(self):
        return reverse('lessons:delete', args=[self.pk])