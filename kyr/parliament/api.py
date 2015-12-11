# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import MemberOfParliament
from rest_framework import generics
from .serializers import MemberOfParliamentSerializer
from rest_framework.permissions import AllowAny


class MemberOfParliamentViewSet(generics.ListAPIView):

    '''
    API Endpoint that allows MP's Parliament Related Details to be viewed
    '''

    permission_classes = (AllowAny, )
    serializer_class = MemberOfParliamentSerializer

    def get_queryset(self):
        """
        This view should return a information about the the particular MP
        whose name is being searched.
        """
        name_of_the_mp = self.kwargs['name_of_the_mp']
        return MemberOfParliament.objects.filter(name_of_the_mp=name_of_the_mp)

# Some Exception Handling Would be Good Here
