from django.db import models
from django.urls import reverse

"""class ModelBase:
    base_Character = []
    pub_data = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now

    def __str__(self):
        return self.base_Character"""


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    battlefield_role = models.CharField(max_length=100, blank=True)
    power_rating = models.CharField(max_length=100, blank=True)
    unit_composition = models.CharField(max_length=100, blank=True)
    wargear = models.TextField(max_length=100, blank=True)
    abilities = models.TextField(max_length=100, blank=True)
    faction_keywords = models.TextField(max_length=100, blank=True)
    keywors = models.TextField(max_length=100, blank=True)
    weapons = models.TextField(max_length=100, blank=True)
    profile = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    '''def get_absolut_url(self):
        return reverse('character', args=[self.pk])'''


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    range = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    strength = models.CharField(max_length=100, blank=True)
    armor_penetration = models.CharField(max_length=100, blank=True)
    damage = models.CharField(max_length=100, blank=True)
    abilities = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name


"""class Roster(models.Model):
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

    def __str__(self):
        return self.group

class Append(models.Model):
    questionOfRoster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    NameOfSolder = models.CharField(max_length=200)

    def __str__(self):
        return self.questionOfRoster, self.NameOfSolder"""
