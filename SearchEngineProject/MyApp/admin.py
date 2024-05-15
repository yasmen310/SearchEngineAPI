from django.contrib import admin
from .models import Track, User, Book, Question, Answer, Note, QuestionAndAnswer

admin.site.register(Track)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Note)
admin.site.register(QuestionAndAnswer)
