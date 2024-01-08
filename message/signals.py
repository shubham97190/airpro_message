import _thread as thread
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.conf import settings
from message.models import Message

def send_mail_all_user(message:Message):
    body = message.body_html
    for id in message.recipients:
        msg = EmailMultiAlternatives(message.subject, body, settings.DEFAULT_FROM_EMAIL, to=[id])
        msg.attach_alternative(body, "text/html")
        msg.send()
@receiver(post_save, sender=Message)
def send_mails(sender, instance, created, **kwargs):
    if created:
        thread.start_new_thread(send_mail_all_user, (instance,))
