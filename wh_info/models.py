from django.db import models

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
    name = models.CharField(max_length=100000)
    description = models.TextField(max_length=100000)
    battlefield_role = models.CharField(max_length=100000)
    power_rating = models.CharField(max_length=100000)
    unit_composition = models.CharField(max_length=100000)
    wargear = models.TextField(max_length=100000)
    abilities = models.TextField(max_length=100000)
    faction_keywords = models.TextField(max_length=100000)
    keywors = models.TextField(max_length=100000)
    weapons = models.TextField(max_length=100000)
    profile = models.TextField(max_length=100000)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=100000)
    range = models.CharField(max_length=100000)
    type = models.CharField(max_length=100000)
    strength = models.CharField(max_length=100000)
    armor_penetration = models.CharField(max_length=100000)
    damage = models.CharField(max_length=100000)
    abilities = models.TextField(max_length=100000)

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
