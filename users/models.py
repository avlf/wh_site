from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have email-adress')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('User must have email-adress')
        superuser = self.model(email=self.normalize_email(email))
        superuser.set_password(password)
        superuser.staff = True
        superuser.admin = True
        superuser.save()
        return superuser


class User(AbstractBaseUser):
    name = models.CharField('User name', max_length=20, blank=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    about = models.TextField('User description', max_length=2000, blank=True)
    # roster = models.ManyToMany(blank=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
