from django.db import models

from wh_info.constants import BATTLEFIELD_ROLE_CHOICE

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
    battlefield_role = models.CharField(max_length=100, choices=BATTLEFIELD_ROLE_CHOICE)
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


class Roster(models.Model):
    character = models.ForeignKey(
        Character,
        related_name='chars',
        related_query_name='char',
        on_delete=models.CASCADE,
        limit_choices_to={'battlefield_role':'commander'},
        null=True
    )
    troops = models.ForeignKey(
        Character,
        related_name='troops',
        related_query_name='troop',
        on_delete=models.CASCADE,
        limit_choices_to={'battlefield_role':'troops'},
        null=True
    )
    elite = models.ForeignKey(
        Character,
        related_name='elites',
        related_query_name='elite',
        on_delete=models.CASCADE,
        limit_choices_to={'battlefield_role': 'elite'},
        null=True
    )
    fast_attack = models.ForeignKey(
        Character,
        related_name='fast_attacks',
        related_query_name='fast_attack',
        on_delete=models.CASCADE,
        limit_choices_to={'battlefield_role': 'fast_attack'},
        null=True
    )
    heavy_support = models.ForeignKey(
        Character,
        related_name='heavy_supports',
        related_query_name='heavy_support',
        on_delete=models.CASCADE,
        limit_choices_to={'battlefield_role': 'heavy_support'},
        null=True
    )
