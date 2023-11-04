import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mail


from mailing.models import Mailing, MailingLog
from mailing.services import send_email


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        now = datetime.datetime.now()
        for mailing in Mailing.objects.filter(status=Mailing.STATUS_STARTED):
            for customer in mailing.customer.all():
                logs = MailingLog.objects.filter(mailing=mailing, mailing__customer=customer)
                if logs.exists():
                    last_try_date = logs.order_by('-last_mailing_time').first()
                    if mailing.period == Mailing.PERIOD_DAILY:
                        if (now - last_try_date).days >= 1:
                            send_email(mailing, customer)
                    elif mailing.period == Mailing.PERIOD_WEEKLY:
                        if (now - last_try_date).days >= 7:
                            send_email(mailing, customer)
                    elif mailing.period == Mailing.PERIOD_MONTHLY:
                        if (now - last_try_date).days >= 30:
                            send_email(mailing, customer)
                else:
                    send_email(mailing, customer)


