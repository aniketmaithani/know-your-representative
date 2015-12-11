# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields
import uuid_upload_path.storage
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberOfParliament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name_of_the_mp', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=100, help_text='State to which MP Belongs')),
                ('photo_of_the_mp', versatileimagefield.fields.VersatileImageField(null=True, upload_to=uuid_upload_path.storage.upload_to, blank=True)),
                ('constituency', models.CharField(max_length=100, help_text='constituency of the mp')),
                ('attendance_percent', models.DecimalField(max_digits=8, decimal_places=2)),
                ('debates_total', models.IntegerField()),
                ('no_of_questions_asked', models.IntegerField()),
                ('private_member_bill_asked', models.IntegerField()),
                ('unique_id', uuidfield.fields.UUIDField(editable=False, unique=True, blank=True, max_length=32)),
            ],
            options={
                'verbose_name': 'MP',
                'verbose_name_plural': 'MPs',
                'ordering': ['-name_of_the_mp'],
            },
        ),
    ]
