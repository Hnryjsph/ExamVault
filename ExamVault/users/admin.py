from django.contrib import admin

from .models import CustomUser, Feedback, FrequentlyAskedQuestion
from .models import TermsAndConditions

# Adding Custom User model to admin
admin.site.register(CustomUser)

# Adding Feedback Model to the admin
admin.site.register(Feedback)

# Adding the FrequentlyAskedQuestions Model to the Admin
admin.site.register(FrequentlyAskedQuestion)

# Adding the TermsAndConditions Model to the Admin
admin.site.register(TermsAndConditions)
