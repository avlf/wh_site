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
    cost = models.CharField(max_length=100, blank=True)
    movement = models.CharField(max_length=100, blank=True)
    weapon_skill = models.CharField(max_length=100, blank=True)
    ballistic_skill = models.CharField(max_length=100, blank=True)
    streath = models.CharField(max_length=100, blank=True)
    tenesity = models.CharField(max_length=100, blank=True)
    wd = models.CharField(max_length=100, blank=True)
    leader = models.CharField(max_length=100, blank=True)
    attack = models.CharField(max_length=100, blank=True)
    spas_roll = models.CharField(max_length=100, blank=True)

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
    char_list = Character.objects.filter(battlefield_role='character')
    character = models.ManyToManyField(
        Character,
        related_name='chars',
        related_query_name=char_list
    )
    troops = models.ManyToManyField(
        Character,
        related_name='troops',

    )
    elite = models.ManyToManyField(
        Character,
        related_name='elites',

    )
    fast_attack = models.ManyToManyField(
        Character,
        related_name='fast_attacks',

    )
    heavy_support = models.ManyToManyField(
        Character,
        related_name='heavy_supports',

    )
    flyers = models.ManyToManyField(
        Character,
        related_name='flyers',

    )
    dedicated_transport = models.ManyToManyField(
        Character,
        related_name='dedicated_transport',

    )
    lords_of_war = models.ManyToManyField(
        Character,
        related_name='lords_of_war',

    )
