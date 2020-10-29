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
    links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField("Username", max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.ord_id)

    def get_absolute_url(self):
        return f'/db_manager/db_manager/{self.ord_id}'


class customer_price(models.Model):
    ord_id = models.IntegerField('Номер заказа', primary_key=True, default=1, null=False, editable=False, unique=False)
    tel_id = models.CharField("Автор", max_length=45, blank=True, null=True, editable=False)
    price = models.CharField("Цена автора", max_length=80, blank=True, null=True)
    com = models.CharField("Комментарий", max_length=2000, blank=True, null=True)
    auth_username = models.CharField("Username", max_length=80, blank=True, null=True)
    customer_pr = models.CharField("Цена для заказчика", max_length=80, blank=True, null=True)
    customer_username = models.CharField("Username заказчика", max_length=80, blank=True, null=True)

    def __str__(self):
        return str(self.ord_id)

    def get_absolute_url(self):
        return f'/db_manager/db_manager/{self.ord_id}'

class cust_pri(models.Model):
    ord_id = models.IntegerField('Номер заказа', primary_key=True, default=1, null=False, editable=False, unique=False)
    tel_id = models.CharField("Автор", max_length=45, blank=True, null=True, editable=False)
    price = models.CharField("Цена автора", max_length=80, blank=True, null=True)
    com = models.CharField("Комментарий", max_length=2000, blank=True, null=True)
    auth_username = models.CharField("Username", max_length=80, blank=True, null=True)
    customer_pr = models.CharField("Цена для заказчика", max_length=80, blank=True, null=True)
    customer_username = models.CharField("Username заказчика", max_length=80, blank=True, null=True)

    def __str__(self):
        return str(self.ord_id)

    def get_absolute_url(self):
        return f'/db_manager/db_manager/{self.ord_id}'

class PriceO(models.Model):
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
    links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')
    payment = models.CharField(blank=True, max_length=100, null=True, verbose_name='Оплата')

    def __str__(self):
        return str(self.ord_id)

class ord_auth_price(models.Model):
    ord_id = models.IntegerField('Номер заказа', null=True, editable=False, unique=False)
    tel_id = models.CharField("Автор", max_length=45, blank=True, null=True, editable=False)
    price = models.CharField("Цена", max_length=80, blank=True, null=True)
    com = models.CharField("Комментарий", max_length=2000, blank=True, null=True)
    auth_username = models.CharField("Username", max_length=80, blank=True, null=True)
    unique = models.IntegerField('Номер заказа', null=False, editable=False, unique=False, primary_key=True, default=1)


    def __str__(self):
        return str(self.ord_id)

    def get_absolute_url(self):
        return f'/db_manager/db_manager/{self.ord_id}'

class ActiveO(models.Model):
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
    links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')
    payment = models.CharField(blank=True, max_length=100, null=True, verbose_name='Оплата')
    author = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')


    def __str__(self):
        return str(self.ord_id)

class waitO(models.Model):
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
    links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')
    payment = models.CharField(blank=True, max_length=100, null=True, verbose_name='Оплата')
    author = models.CharField("Ссылки на документы", max_length=500, blank=True, null=True)
    author_links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)

    def __str__(self):
        return str(self.ord_id)

class doneO(models.Model):
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
    links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')
    payment = models.CharField(blank=True, max_length=100, null=True, verbose_name='Оплата')
    author_links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    otz = models.CharField(blank=True, max_length=100, null=True, verbose_name='Оценка')
    com = models.CharField(blank=True, max_length=2000, null=True, verbose_name='Комментарий')


    def __str__(self):
        return str(self.ord_id)

class canceledo(models.Model):
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
    links = models.CharField("Ссылки на документы", max_length=5000, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')
    payment = models.CharField(blank=True, max_length=100, null=True, verbose_name='Оплата')
    why = models.CharField("Причина", max_length=5000, blank=True, null=True)

    def __str__(self):
        return str(self.ord_id)

class DPO(models.Model):
    ord_id = models.IntegerField('Номер заказа', primary_key=True, editable=False)
    username = models.CharField("username Авторa", max_length=300, blank=True, null=True)
    cost = models.CharField("стоимость работы автора", max_length=45, blank=True, null=True)
    card_num = models.CharField("Номер карты", max_length=45, blank=True, null=True)
    fio = models.CharField("ФИО автора", max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.ord_id)
