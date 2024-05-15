from rest_framework import serializers
from .models import Track, User, Book, Question, Answer, Note, QuestionAndAnswer

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['username', 'name','password', 'email']

class BookSerializer(serializers.ModelSerializer):
    track_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['book_id', 'book_name', 'description', 'book_url', 'track_name','user_name', 'author', 'book_rate','username','track']
  
    def get_track_name(self, obj):
        return obj.track.track_name
    def get_user_name(self, obj):
        return obj.username.name

class QuestionSerializer(serializers.ModelSerializer):
    track_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id','question_content', 'track_name', 'user_name','username','track']

    def get_track_name(self, obj):
        return obj.track.track_name
    def get_user_name(self, obj):
        return obj.username.name


class AnswerSerializer(serializers.ModelSerializer):
    question_content = serializers.SerializerMethodField()
    class Meta:
        model = Answer
        fields = ['id','answer_content','question_content','question']
    def get_question_content(self, obj):
        return obj.question.question_content


class NoteSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = ['id','note_content','user_name','username']
    def get_user_name(self, obj):
        return obj.username.name

class QuestionAndAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAndAnswer
        fields = '__all__'
