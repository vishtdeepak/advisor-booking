from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Advisor(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    profile_photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class AdvisorBooking(models.Model):
    advisor = models.ForeignKey(Advisor, related_name='booking_advisor_date', on_delete=models.CASCADE)
    booking_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.advisor} Booking at {self.booking_time}'

