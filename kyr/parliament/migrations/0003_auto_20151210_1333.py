# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0002_remove_memberofparliament_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberofparliament',
            name='attendance_percent',
            field=models.DecimalField(max_digits=8, decimal_places=2, null=True),
        ),
    ]
