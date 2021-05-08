# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import login, authenticate
# Create your models here.

class Order(models.Model):
    orderid = models.CharField(primary_key = True, max_length = 10)
    name = models.CharField(max_length = 40)
    details = models.TextField()
    status = models.CharField(max_length=10)
    date_ordered = models.DateTimeField(default = timezone.now) 

class Statement(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=400)

    def __str__(self):
        if len(self.text.strip()) > 60:
            return '{}...'.format(self.text[:57])
        elif len(self.text.strip()) > 0:
            return self.text

        return '<empty>'


class Response(models.Model):
    id = models.AutoField(primary_key=True)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    response = models.CharField(max_length=400)

    created_at = models.DateTimeField(
        default=timezone.now,
        help_text='The date and time that this statement was created at.'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        help_text='The date and time that this response was created at.'
    )

    def __str__(self):
        statement = self.statement.text
        response = self.response
        return '{} => {}'.format(
            statement if len(statement) <= 20 else statement[:17] + '...',
            response if len(response) <= 40 else response[:37] + '...'
        )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(primary_key = True, max_length=150)
    def __str__(self):
        return self.user.username
