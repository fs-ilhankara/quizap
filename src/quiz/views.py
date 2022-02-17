
from django.shortcuts import render
from rest_framework import generics
from .models import Category, Question, Quiz 
from .serializers import CategoryDetailSerializer, CategorySerializer, QuestionSerializer
from .pagination import MyPagination
#from rest_framework.permissions import IsAuthenticated, AllowAny
#from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    #permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]


class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs["category"] 
        # backend, frontend url de yazacağımz kategoriye göre filtreleme yapacagız
        queryset = queryset.filter(category__name=category)
        # category ısımlerıne ulasarak fılter yapacagız.iki tane underscore koyduğumuz zaman Category modelindekı tüm fieldlere ulaşabiliyoruz.Category ile foreginkey olan degıskenı secıyoruz.
        return queryset

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    #permission_classes = [IsAuthenticated]
    pagination_class = MyPagination
    

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)
        return queryset