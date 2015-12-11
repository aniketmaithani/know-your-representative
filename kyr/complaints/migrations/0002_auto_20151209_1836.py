# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='description_of_the_problem',
            field=models.CharField(max_length=100, help_text='Description of the problem'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='phone_number_of_the_complainee',
            field=models.CharField(max_length=100, help_text='Phone Number of the Complainee'),
        ),
    ]
