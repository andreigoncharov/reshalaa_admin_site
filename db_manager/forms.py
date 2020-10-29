from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateInput, TimeInput, Select, NumberInput

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['tel_id', 'type', 'prof', 'predm', 'info',
                  'oforml', 'date', 'time', 'end_contr', 'price', 'links', 'username']

        widgets = {

            "tel_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telegram ID заказчика'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип работы'
            }),
            "prof": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профиль'
            }),
            "predm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предмет'
            }),
            "info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о заказе'
            }),
            "oforml": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оформление'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата сдачи'
            }),
            "time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время сдачи'
            }),
            "end_contr": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время окончания контроля'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "links": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылки на документы'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username заказчика'
            })
        }

class UpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['tel_id', 'type', 'prof', 'predm', 'info',
                  'oforml', 'date', 'time', 'end_contr', 'price', 'links', 'username']

        widgets = {

            "tel_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telegram ID заказчика'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип работы'
            }),
            "prof": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профиль'
            }),
            "predm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предмет'
            }),
            "info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о заказе'
            }),
            "oforml": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оформление'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата сдачи'
            }),
            "time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время сдачи'
            }),
            "end_contr": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время окончания контроля'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "links": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылки на документы'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username заказчика'
            })
        }

class WUpdateForm(ModelForm):
    class Meta:
        model = waitO
        fields = ['type', 'prof', 'predm', 'info',
                  'oforml', 'date', 'time', 'end_contr', 'price', 'links', 'username', 'payment', 'author_links']

        widgets = {
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип работы'
            }),
            "prof": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профиль'
            }),
            "predm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предмет'
            }),
            "info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о заказе'
            }),
            "oforml": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оформление'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата сдачи'
            }),
            "time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время сдачи'
            }),
            "end_contr": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время окончания контроля'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "links": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылки на документы'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username заказчика'
            }),
            "author_links": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Username заказчика'
            }),
        }

class PriceForm(ModelForm):
    class Meta:
        model = customer_price
        fields = ['auth_username', 'com', 'price']

        widgets = {

            "auth_username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "com": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })
        }