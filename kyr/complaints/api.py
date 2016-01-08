# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import Complaints
from .serializers import ComplaintSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class ComplaintViewSet(generics.UpdateAPIView, generics.DestroyAPIView, generics.CreateAPIView):

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        complaint = Complaints.objects.get(pk=pk)
        serializer = ComplaintSerializer(complaint, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            complaint.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        complaint = Complaints.objects.get(pk=pk)
        serializer = ComplaintSerializer(complaint)
        if serializer.is_valid():
            serializer.save()
            complaint.delete()
            return Response({"response": "deleted"})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
