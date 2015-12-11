# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuidfield.fields
import versatileimagefield.fields
import uuid_upload_path.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_the_complainee', models.CharField(max_length=256)),
                ('phone_number_of_the_complainee', models.CharField(help_text=b'Phone Number of the Complainee', max_length=100)),
                ('photo_of_the_area', versatileimagefield.fields.VersatileImageField(null=True, upload_to=uuid_upload_path.storage.upload_to, blank=True)),
                ('description_of_the_problem', models.CharField(help_text=b'Description of the problem', max_length=100)),
                ('geolocation', models.CharField(max_length=256)),
                ('name_of_the_mp_for_problem_redressal', models.CharField(max_length=256)),
                ('unique_complain_id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
            ],
            options={
                'ordering': ['-unique_complain_id'],
                'verbose_name': 'Complain',
                'verbose_name_plural': 'Complaints',
            },
        ),
    ]
