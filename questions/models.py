from django.db import models
from django.shortcuts import reverse

from lessons.models import Lesson


class Test(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse('questions:delete', args=[self.pk])

    def get_edit_url(self):
        return reverse('questions:edit', args=[self.pk])


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)

    def __str__(self):
        return self.question
