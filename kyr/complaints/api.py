# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import Complaints
from .serializers import ComplaintSerializer
from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny


class ComplaintViewSet(mixins.CreateModelMixin, generics.GenericAPIView):

    """
    API endpoint that allows user to submit their complaints
    """
    permission_classes = (AllowAny, )
    queryset = Complaints.objects.all()
    serializer_class = ComplaintSerializer
