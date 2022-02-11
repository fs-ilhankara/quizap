from django.contrib import admin
from .models import Category, Question, Quiz, Answer
import nested_admin

class AnswerInline(nested_admin.NestedTabularInline):#başka bir tablonun altına girecek olarak hazırla
    model = Answer

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline] #question tablosunun içine answer ekle bunları inline olarak hazırla


class QuizAdmin(nested_admin.NestedModelAdmin):# artık bu tabloları inline olarak burada göstereceğim.
    model = Quiz
    inlines = [QuestionInline]





admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)


# Register your models here.
