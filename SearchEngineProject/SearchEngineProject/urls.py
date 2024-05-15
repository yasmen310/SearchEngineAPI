"""
URL configuration for SearchEngineProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('login/', views.login),
    path('test_token/', views.test_token),
    path('api/tracks/', views.TrackListCreate.as_view()),
    path('api/tracks/<pk>/', views.TrackRetrieveUpdateDestroy.as_view()),
    path('api/users/', views.UserListCreate.as_view()),
    path('api/users/<pk>/', views.UserRetrieveUpdateDestroy.as_view()),
    path('api/books/', views.BookListCreate.as_view()),
    path('api/books/<pk>/', views.BookRetrieveUpdateDestroy.as_view()),
    path('api/questions/', views.QuestionListCreate.as_view()),
    path('api/questions/<pk>/', views.QuestionRetrieveUpdateDestroy.as_view()),
    path('api/answers/', views.AnswerListCreate.as_view()),
    path('api/answers/<pk>/', views.AnswerRetrieveUpdateDestroy.as_view()),
    path('api/notes/', views.NoteListCreate.as_view()),
    path('api/notes/<pk>/', views.NoteRetrieveUpdateDestroy.as_view()),
    path('api/question-and-answers/', views.QuestionAndAnswerListCreate.as_view()),
    path('api/question-and-answers/<pk>/', views.QuestionAndAnswerRetrieveUpdateDestroy.as_view()),
]

