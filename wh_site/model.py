import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

class List(models.Model):
    stats = models.CharField(max_length=100000)
    pub_data = models.DateTimeField('date published')
    @admin.display(
        boolean =True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now

class Roster:
    group = []
    pub_data = models.DateTimeField('date published')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now


class Append(models.Model):
    questionOfRoster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    NameOfSolder = models.CharField(max_length=200)


    def __str__(self):
        return self.questionOfRoster, self.NameOfSolder
