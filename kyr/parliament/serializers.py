from . import models
from rest_framework import serializers


class MemberOfParliamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MemberOfParliament
        fields = ('name_of_the_mp', 'state', 'photo_of_the_mp', 'constituency', 'attendance_percent',
                  'debates_total', 'no_of_questions_asked', 'private_member_bill_asked',)
