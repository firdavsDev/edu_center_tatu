from django.db.models.signals import post_save
from django.dispatch import receiver


from .alerter import tg_alert
from .models import Contact


@receiver(post_save, sender=Contact)
def create_contact(sender, instance, created, **kwargs):
    if created:
        tg_alert.custom_alert(
            text=f'Yangi xabarchi ismi: {instance.name}\n\nXabar: {instance.message}')
