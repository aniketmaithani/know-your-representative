# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from versatileimagefield.fields import VersatileImageField
from uuid_upload_path import upload_to
from uuidfield import UUIDField


class Complaints(models.Model):
    name_of_the_complainee = models.CharField(
        blank=False, null=False, max_length=256)
    phone_number_of_the_complainee = models.CharField(blank=False, null=False,
                                                      max_length=100, help_text='Phone Number of the Complainee')
    photo_of_the_area = VersatileImageField(
        blank=True, null=True, upload_to=upload_to)
    description_of_the_problem = models.CharField(blank=False, null=False,
                                                  max_length=100, help_text='Description of the problem')
    geolocation = models.CharField(blank=False, null=False, max_length=256)
    name_of_the_mp_for_problem_redressal = models.CharField(
        blank=False, null=False, max_length=256)
    unique_complain_id = UUIDField(auto=True)

    def __str__(self):
        return self.name_of_the_complainee

    class Meta:
        verbose_name = "Complain"
        verbose_name_plural = "Complaints"
        ordering = ['-unique_complain_id']
