from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    email = models.EmailField(max_length=100, verbose_name='email', unique=True)
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f"email: {self.email}, ФИО: {self.full_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_DONE, 'Завершена'),
    )

    time = models.DateTimeField(verbose_name='время рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='периодичность', **NULLABLE)
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус рассылки', **NULLABLE)

    theme = models.CharField(max_length=150, verbose_name='тема')
    mailing_text = models.TextField(verbose_name='текст письма', **NULLABLE)

    customer = models.ManyToManyField(Customer, max_length=150, verbose_name='клиент')

    def __str__(self):
        return f'theme: {self.theme}, period: {self.period}, status: {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    last_try = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now_add=True)
    last_try_status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_OK)
    customer = models.ForeignKey(Customer, max_length=150, verbose_name='клиент', on_delete=models.CASCADE)
    mailing = models.ForeignKey(Mailing, max_length=150, verbose_name='рассылка', on_delete=models.CASCADE)
    error_msg = models.TextField(verbose_name='error message', **NULLABLE)

    def __str__(self):
        return f'{self.mailing} {self.last_try} {self.last_try_status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'








