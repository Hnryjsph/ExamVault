from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def subscription(request):
	context = {}
	return render(request, 'subscriptions.html', context)