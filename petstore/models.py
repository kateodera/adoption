# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pet(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=200)
    submitter = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('vaccine', blank=True)

    class Meta:
        verbose_name = "pet"
        verbose_name_plural = "pets"

    def __str__(self):
        return str(self.name)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
