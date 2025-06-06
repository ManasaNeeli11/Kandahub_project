from django.contrib import admin
from .models import Quiz, Question, Choice, UserQuizResponse

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserQuizResponse)
