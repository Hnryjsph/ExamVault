from django.contrib import admin

from .models import CustomUser, Feedback, FrequentlyAskedQuestion



admin.site.register(CustomUser)
admin.site.register(Feedback)
admin.site.register(FrequentlyAskedQuestion)