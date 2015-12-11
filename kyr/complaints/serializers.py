from rest_framework import serializers

from . import models


class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Complaints
        fields = ('name_of_the_complainee', 'phone_number_of_the_complainee', 'photo_of_the_area', 'geolocation',
                  'description_of_the_problem', 'name_of_the_mp_for_problem_redressal')
