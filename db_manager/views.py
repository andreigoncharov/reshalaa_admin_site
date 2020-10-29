import asyncio

from aiogram import Bot
from aiogram.types import inline_keyboard
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import *
from .scripts import *

BOT_TOKEN = '1304714679:AAHLFh5t6qAhBhwgzWdnp9n7A8GpY_uKXuo'
BOT_URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN
BOT_CHAT_ID = ''


async def send_message(chat_id, text=None, keyboard=None, token=BOT_TOKEN):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard, parse_mode='html')
    return


def orderInfo(request):
    order = Order.objects.all()
    return render(request, 'db_manager/orderInfo.html', {'order': order})


def create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wo')

    form = OrderForm()

    data = {
        'form': form
    }
    return render(request, 'db_manager/create.html', data)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'db_manager/order_detail.html'
    context_object_name = 'dorder'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auth'] = ord_auth_price.objects.all()

        return context


class AOrderDetailView(DetailView):
    model = ActiveO
    template_name = 'db_manager/orderInfo.html'
    context_object_name = 'dorder'


class WOrderDetailView(DetailView):
    model = waitO
    template_name = 'db_manager/w_orderInfo.html'
    context_object_name = 'dorder'

class DorderDetailView(DetailView):
    model = doneO
    template_name = 'db_manager/d_order.html'
    context_object_name = 'dorder'

class CorderDetailView(DetailView):
    model = canceledo
    template_name = 'db_manager/c_order.html'
    context_object_name = 'dorder'

class OrderUpdateView(UpdateView):
    model = Order
    form_class = UpdateForm
    template_name = 'db_manager/update.html'
    success_url = reverse_lazy('wo')

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_text())


class WOrderUpdateView(UpdateView):
    model = waitO
    form_class = UpdateForm
    template_name = 'db_manager/updatewo.html'
    success_url = reverse_lazy('waitOh')


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('wo')
    template_name = 'db_manager/delete_o.html'


def confirm_price(request):
    ord_id = request.GET.get("id", False)
    data = ord_id.split('?')
    ord_id = data[0]
    auth = data[1].replace('auth=', '')

    tel_id = send_price_c(ord_id, auth)
    print(tel_id)
    cost, bonuses = get_new_cost(tel_id, ord_id)

    k = inline_keyboard.InlineKeyboardMarkup()
    k.add(inline_keyboard.InlineKeyboardButton('💰Оплатить 💰', callback_data=f'pay_{ord_id}'))
    k.add(inline_keyboard.InlineKeyboardButton('💰Оплатить c бонусами 💰', callback_data=f'payb_{ord_id}'))
    k.add(inline_keyboard.InlineKeyboardButton('❌ Отменить заказ ❌', callback_data=f'otmena_{ord_id}'))

    price = cost
    p_price = round(int(price) * (50 / 100))

    text = '<b>Мы оценили заказ и готовы его выполнить!</b> 🚀' \
           f'\n<b>Заказ № {ord_id}</b>\n\n' \
           f'➡️ <b>К оплате: {price} грн.</b>  ⬅️\n' \
           f'Для начала работы можно внести предоплату в размере {p_price} грн.\n\n' \
           f'На вашем счету есть бонусы в размере <i>{bonuses}</i> грн. Вы можете их использовать!\n\n' \
           '⚠️ Предложение действительно в течении 24 часов ⚠️'

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_message(tel_id[0], text=text, keyboard=k))

    return render(request, 'db_manager/wo_1.html')


def confandsend(request):
    ord_id = request.GET.get("id", False)
    data = ord_id.split('?')
    ord_id = data[0]

    payment, tel_id, files = check_and_send_order(ord_id)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    k = inline_keyboard.InlineKeyboardMarkup()
    k.add(inline_keyboard.InlineKeyboardButton('Связь с менеджером 📱', callback_data='manager'))

    if payment == 1:
        text = f'🎊 <b>Ваша робота готова!</b> 🎊\n' \
               f'Заказ №{ord_id}'
        loop.run_until_complete(send_message(tel_id, text=text))

        file = files.split(' , ')
        for f in file:
            if f == '':
                 a = ''
            else:
                loop.run_until_complete(send_message(tel_id, text=f))

        text_2 = '❤️ <b>Спасибо, что вы с Reshalla</b>\n' \
                 ' ❤️<b>Желаем удачи со сдачей работы!</b>\n' \
                 'Есть вопросы? 👇'
        loop.run_until_complete(send_message(tel_id, text=text_2, keyboard=k))

        text_3 = '<b>Насколько Вы довольны нашей работой?</b>\n' \
                 'Выберите цифру от 1 до 5	🙌'
        loop.run_until_complete(send_message(tel_id, text=text_3, keyboard=otz(ord_id)))

    else:
        text = f'<b>Ваш заказ №{ord_id} готов!\n\n</b>' \
               f'❗️Пожалуйста, внесите доплату, чтобы получить готовую работу\n️' \
               f'➡️ <b>К доплате: {payment} грн.</b>  ⬅️'
        k1 = inline_keyboard.InlineKeyboardMarkup()
        k1.add(inline_keyboard.InlineKeyboardButton('💰Оплатить 💰', callback_data=f'paytwo_{ord_id}'))
        loop.run_until_complete(send_message(tel_id, text=text, keyboard=k1))
    return render(request, 'db_manager/wo_1.html')

def otz(ord_id):
    k = inline_keyboard.InlineKeyboardMarkup()
    one = inline_keyboard.InlineKeyboardButton('1️⃣', callback_data=f'one_{ord_id}')
    two = inline_keyboard.InlineKeyboardButton('2️⃣', callback_data=f'two_{ord_id}')
    three = inline_keyboard.InlineKeyboardButton('3️⃣', callback_data=f'three_{ord_id}')
    four = inline_keyboard.InlineKeyboardButton('4️⃣', callback_data=f'four_{ord_id}')
    five = inline_keyboard.InlineKeyboardButton('5️⃣', callback_data=f'five_{ord_id}')
    k.row(one, two, three, four, five)
    return k

def payok(request):
    ord_id = request.GET.get("id", False)
    data = ord_id.split('?')
    ord_id = data[0]

    payok_db(ord_id)
    order = Order.objects.all()

    return render(request, 'orders/wo.html', {'order': order})


def index(request):
    order = Order.objects.all()
    return render(request, 'orders/wo.html', {'order': order})


def priceO(request):
    order = cust_pri.objects.all()
    return render(request, 'db_manager/priceO.html', {'order': order})

def wo_1(request):
    order = Order.objects.all()
    return render(request, 'db_manager/wo_1.html', {'order': order})


def activeO(request):
    orders = ActiveO.objects.all()
    return render(request, 'orders/activeO.html', {'order': orders})


def canceledO(request):
    orders = canceledo.objects.all()
    return render(request, 'orders/canceledO.html', {'order': orders})


def waitOh(request):
    order = waitO.objects.all()
    return render(request, 'orders/waitOh.html', {'order': order})


def DpO(request):
    info = DPO.objects.all()
    return render(request, 'orders/pay.html', {'info': info})

def DoneO(request):
    order = doneO.objects.all()
    return render(request, 'orders/doneO.html', {'order': order})


class ActiveOrderDetailView(DetailView):
    model = ActiveO
    template_name = 'db_manager/orderInfo.html'
    context_object_name = 'dorder'

#            <a href="{% url 'create' %}"><li><button class="btn btn-info"><i class="fas fa-plus-circle"> Добавить заказ</i></button></li></a>
