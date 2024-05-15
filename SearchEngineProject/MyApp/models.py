from django.db import models
from django.core.validators import RegexValidator

class Track(models.Model):
    track_id = models.CharField(primary_key=True, max_length=6, validators=[
        RegexValidator(r'^\d{6}$', 'Track_id must be exactly 6 digits')
    ])
    track_name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.track_name

class User(models.Model):
    username =models.CharField(primary_key=True, max_length=8 ,validators=[
        RegexValidator(r'^\d{8}$', 'User_id must be exactly 8 digits')
    ])
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25, validators=[
        RegexValidator(
                regex='^(?=.*[0-9])(?=.*[a-zA-Z]).{8,}$',
                message='Password must contain at least one digit and one character, and be at least 8 characters long.',
                code='invalid_password'
            )
    ])

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id =  models.CharField(primary_key=True, max_length=4 ,validators=[
        RegexValidator(r'^\d{4}$', 'Book_id must be exactly 4 digits')
    ])
    book_name = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    book_url = models.URLField(blank=True, null=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    author =  models.CharField(max_length=50)
    username= models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    book_rate = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.book_name

class Question(models.Model):
    question_content = models.TextField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_content

class Answer(models.Model):
    answer_content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_content

class Note(models.Model):
    note_content = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_content

class QuestionAndAnswer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)