from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = [
	('1', 'male'),
	('2', "female")
]

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length = 5, choices = GENDER_CHOICES, default = '1')
    # Add other custom fields as needed

    def __str__(self):
        return self.username
