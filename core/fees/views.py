from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import generics
from fees.models import StudentFee,FeeStructure
from fees.serializers import StudentFeeSerializer,FeeStructureSerializer
from accounts.permissions import IsAdminUser

class FeeStructureListCreateAPIView(generics.ListCreateAPIView):
    queryset=FeeStructure.objects.all()
    serializer_class=FeeStructureSerializer
    permission_classes=[IsAdminUser]

class FeeStructureRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    lookup_field = "id"
    permission_classes = [IsAdminUser]
class StudentFeeListCreateAPIView(generics.ListCreateAPIView):

    queryset = StudentFee.objects.select_related("student").prefetch_related("fee_structures")
    serializer_class = StudentFeeSerializer
    permission_classes = [IsAdminUser]


class StudentFeeRetrieveAPIView(generics.RetrieveAPIView):

    queryset = StudentFee.objects.select_related("student").prefetch_related("fee_structures")
    serializer_class = StudentFeeSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]