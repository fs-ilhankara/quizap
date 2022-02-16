
from django.shortcuts import render
from rest_framework import generics
from .models import Category 
from .serializers import CategorySerializer
# from .pagination import MyPagination
#from rest_framework.permissions import IsAuthenticated, AllowAny
#from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class Category(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    #permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
