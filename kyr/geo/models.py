# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class Constituency(models.Model):
    constituency_name = models.CharField(
        blank=False, null=False, max_length=256)
    state = models.CharField(blank=False, null=False,
                             max_length=100, help_text='State Where constituency lies')

    def __str__(self):
        return self.constituency_name

    class Meta:
        verbose_name = "Constituency"
        verbose_name_plural = "Constituencies"
        ordering = ['-constituency_name']
