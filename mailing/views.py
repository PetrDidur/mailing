from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import MailingForm, CustomerForm
from mailing.models import Mailing, MailingLog, Customer


class MailingList(ListView):
    model = Mailing

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mailing List'
        return context


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:index')


class MailingLogList(ListView):
    model = MailingLog
    template_name = 'mailing/mailinglog_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(mailing__status=Mailing.STATUS_DONE)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mailing Logs  List'
        return context


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:mailing_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:index')


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm

    success_url = reverse_lazy('mailing:index')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm

    success_url = reverse_lazy('mailing:index')


class CustomerList(ListView):
    model = Customer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customer List'
        return context


class CustomerDetailView(DetailView):
    model = Customer


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('mailing:customer_list')

