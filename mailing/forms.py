from django import forms

from mailing.models import Mailing, Customer

from django import forms


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-basic'
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs['class'] = 'form-control datepicker'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-time'
            elif isinstance(field.widget, forms.widgets.SelectMultiple):
                field.widget.attrs['class'] = 'form-control select2 select2-multiple'
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = 'form-control select2'
            elif isinstance(field.widget, forms.widgets.PasswordInput):
                field.widget.attrs['class'] = 'form-control'

            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'


class CustomerForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
