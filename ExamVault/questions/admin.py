from django.contrib import admin

from .models import Question, Collection


# Adding the Question model to the Admin
admin.site.register(Question)

# Adding the Collection model to the Admin
admin.site.register(Collection)