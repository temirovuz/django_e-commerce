from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    TYPE_USERS = (
        (1, 'SuperAdmin'),
        (2, 'Admin'),
        (3, 'Customer'),
        (4, 'Salesman')
    )

    user_type = models.PositiveSmallIntegerField(choices=TYPE_USERS, default=3)
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.username


class Company(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Address(TimeStampedModel):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Seller(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller', null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='seller', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='seller', null=True)

    def __str__(self):
        return self.user.username

