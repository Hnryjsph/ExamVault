from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = [
	('1', 'male'),
	('2', "female")
]

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length = 5, choices = GENDER_CHOICES, default = '1')
    course = models.CharField(max_length = 50, default = 'None')
    university = models.CharField(max_length = 50, default = 'None')
    country = models.CharField(max_length = 50, default = 'Uganda')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Add other custom fields as needed

    def __str__(self):
        return self.username

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.user.username}"


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
