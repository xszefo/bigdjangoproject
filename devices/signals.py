from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DataCenter

#@receiver(post_save, sender=DataCenter)
def display_signal(sender, instance, **kwargs):
	print('POST SAVE')
	print(instance.name)
#post_save.connect(receiver=display_signal, sender=DataCenter)


