from django.conf import settings
from django.core.mail import send_mail

from mailing.models import MailingLog


def send_email(mailing, customer):
    result = send_mail(
        subject=mailing.theme,
        message=mailing.mailing_text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[customer.email],
        fail_silently=False
    )

    MailingLog.objects.create(
        last_try_status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
        mailing=mailing,
        customer=customer
    )
    

