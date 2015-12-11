# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import Complaints
from .serializers import ComplaintSerializer
from rest_framework import generics, mixins, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class ComplaintViewSet(mixins.CreateModelMixin,
                       generics.GenericAPIView):

    """
    API endpoint that allows user to submit their complaints
    """
    permission_classes = (AllowAny, )
    serializer_class = ComplaintSerializer
    queryset = Complaints.objects.all()

    def post(self, request, format=None):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
