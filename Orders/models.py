from django.db import models

from django.db import models

class Order(models.Model):
    ord_id = models.IntegerField('Номер заказа', primary_key=True, editable=False)
    tel_id = models.CharField("Заказчик", max_length=45, blank=True, null=True)
    type = models.CharField("Тип", max_length=80, blank=True, null=True)
    prof = models.CharField("Профиль", max_length=80, blank=True, null=True)
    predm = models.CharField("Предмет", max_length=80, blank=True, null=True)
    info = models.CharField("Информация", max_length=3000, blank=True, null=True)
    oforml = models.CharField("Оформление", max_length=60, blank=True, null=True)
    date = models.CharField("Дата сдачи", max_length=45, blank=True, null=True)
    time = models.CharField("Время сдачи", max_length=45, blank=True, null=True)
    end_contr = models.CharField("Окончание контроля", max_length=45, blank=True, null=True)
    price = models.CharField("Цена", max_length=45, blank=True, null=True)
    links = models.URLField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')

    def __str__(self):
        return str(self.ord_id)
