from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification
from users.models import CustomUser

@login_required
def notifications(request):
	if request.method == 'POST':
		if request.POST['check'] == 'true':
			notif = Notification.objects.get(id = int(request.POST['id']))
			notif.delete_notification(request.user)
			notif.save()

			return redirect('/notifications/')

	user = CustomUser(id = request.user.id)
	notifs = Notification.objects.filter(recipients=user)
	context = {"notifications": notifs}
	return render(request, 'notifications.html', context)