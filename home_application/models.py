# -*- coding: utf-8 -*-

from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    CODE = models.CharField(max_length=100, default='')