# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0003_auto_20151210_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberofparliament',
            name='debates_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='memberofparliament',
            name='no_of_questions_asked',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='memberofparliament',
            name='private_member_bill_asked',
            field=models.IntegerField(null=True),
        ),
    ]
