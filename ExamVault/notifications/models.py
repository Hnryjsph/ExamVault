from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    message = models.CharField(max_length=255)
    recipients = models.ManyToManyField(CustomUser, blank=True, related_name='notifications')
    send_to_all = models.BooleanField(default=False)
   

    def __str__(self):
        return self.message

    # Overriding the save function 
    def save(self, *args, **kwargs):
    	super().save(*args, **kwargs)

    	self.send_notification()

    def send_notification(self):
        if self.send_to_all:
            recipients = CustomUser.objects.all()
        else:
            recipients = self.recipients.all()

        # Send the notification to each recipient
        for recipient in recipients:
            self.recipients.add(recipient)
            #self.save()

    def delete_notification(self, user):
        
        self.recipients.remove(user)

        # Delete the notification if it has no more recipients or has been seen by all recipients
        if self.recipients.count() == 0:
            self.delete()
