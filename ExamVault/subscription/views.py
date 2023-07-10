from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# A View that handles subscription functionality
@login_required
def subscription(request):
	context = {}
	return render(request, 'subscriptions.html', context)