from django.db import models
from django_jsonform.models.fields import ArrayField

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
    view = models.CharField(max_length=100, blank=True)
    unit_composition = models.CharField(max_length=100, blank=True)
    wargear = ArrayField(
        models.CharField(max_length=300, blank=True),
        blank=True
    )
    abilities = ArrayField(
        models.TextField(max_length=300, blank=True),
        blank=True
    )

    faction_keywords = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True
    )

    keywors = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True
    )

    weapons = models.TextField(max_length=100, blank=True)
    profile = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    '''def get_absolut_url(self):
        return reverse('character', args=[self.pk])'''

    def showStats(self):
        stats = {'c': self.cost, 'm': self.movement, 'w': self.weapon_skill, 'b': self.ballistic_skill,
                 's': self.streath}
        return stats


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
    name = models.CharField('Roster name', max_length=100)
    commanders = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'commander'},
        related_name='commander'
    )
    troops = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'troops'},
        related_name='troop'

    )
    elites = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'elite'},
        blank=True,
        related_name='elite'
    )

    fast_attacks = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'fast_attack'},
        blank=True,
        related_name='fast_attack'
    )

    heavy_supports = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'heavy_support'},
        blank=True,
        related_name='heavy_support'
    )

    flyers = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'flyers'},
        blank=True,
        related_name='flyer'
    )

    def __str__(self):
        return self.name


"""class MinRoster(models.Model):
    commanders = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'commander'},
        related_name='commander'
    )
    troops = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'troops'},
        related_name='troop'

    )
    elites = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'elite'},
        blank=True,
        related_name='elite'
    )

    fast_attacks = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'fast_attack'},
        blank=True,
        related_name='fast_attack'
    )

    heavy_supports = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'heavy_support'},
        blank=True,
        related_name='heavy_support'
    )

    flyers = models.ManyToManyField(
        Character,
        limit_choices_to={"battlefield_role": 'flyers'},
        blank=True,
        related_name='flyer'
    )


class Battalion(MinRoster):
    com3 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'commander'},
        related_name='com3'
    )
    tro4 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'troops'},
        related_name='tro4'

    )
    tro5 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'troops'},
        related_name='tro5'
    )
    tro6 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'troops'},
        null=True,
        blank=True,
        related_name='tro6'
    )
    elite3 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'elite'},
        null=True,
        blank=True,
        related_name='elite3'
    )
    elite4 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'elite'},
        null=True,
        blank=True,
        related_name='elite4'
    )
    elite5 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'elite'},
        null=True,
        blank=True,
        related_name='elite5'
    )
    elite6 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'elite'},
        null=True,
        blank=True,
        related_name='elite6'
    )
    fast_attack3 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'fast_attack'},
        null=True,
        blank=True,
        related_name='fast_attack3'
    )

    heavy_support3 = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        limit_choices_to={"battlefield_role": 'heavy_support'},
        null=True,
        blank=True,
        related_name='heavy_support3'
    )

    class Meta:
        ordering = ('id',)"""
