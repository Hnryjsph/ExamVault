from django.db import models
from users.models import CustomUser


class Question(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.FileField(upload_to='question_content')
    content_form_text = models.TextField()
    is_verified = models.BooleanField(default=False)
    expert = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='verified_questions')
    timestamp = models.DateTimeField(auto_now_add=True)
    # Other fields related to the question

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
