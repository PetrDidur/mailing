from django.contrib import admin

from mailing.models import Mailing, Customer, MailingLog

admin.site.register(Mailing)
admin.site.register(Customer)
admin.site.register(MailingLog)