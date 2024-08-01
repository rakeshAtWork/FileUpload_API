from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class StudentListCreateView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
