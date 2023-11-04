from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingList, MailingCreateView, MailingLogList, MailingDetailView, MailingUpdateView, \
    MailingDeleteView, CustomerCreateView, CustomerUpdateView, CustomerList, CustomerDetailView, CustomerDeleteView

app_name = MailingConfig.name


urlpatterns = [
    path('', MailingList.as_view(), name='index'),
    path('mailinglog_list/', MailingLogList.as_view(), name='mailinglog_list'),
    path('customer_list/', CustomerList.as_view(), name='customer_list'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
    path('mailing/view/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('customer/view/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('mailing/edit/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('customer/edit/<int:pk>', CustomerUpdateView.as_view(), name='customer_update'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('customer/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer_delete')
]