from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='orderInfo'),
    path('create', views.create, name='create'),
    path('db_manager/<int:pk>/', views.OrderDetailView.as_view(), name='detail_o'),
    path('db_manager/<int:pk>/update', views.OrderUpdateView.as_view(), name='update_o'),
    path('db_manager/<int:pk>/updatew', views.WOrderUpdateView.as_view(), name='update_wo'),
    path('db_manager/<int:pk>/delete', views.OrderDeleteView.as_view(), name='delete_o'),

    path('confirm/', views.confirm_price, name='confirm'),
    path('confandsend/', views.confandsend, name='confandsend'),
    path('payok/', views.payok, name='payok'),

    path('db_manager/detail/<int:pk>/', views.AOrderDetailView.as_view(), name='detail_ao'),
    path('db_manager/detailw/<int:pk>/', views.WOrderDetailView.as_view(), name='detail_wo'),
    path('db_manager/detaildone/<int:pk>/', views.DorderDetailView.as_view(), name='detail_do'),
    path('db_manager/detailco/<int:pk>/', views.CorderDetailView.as_view(), name='detail_co'),

    path('', views.index, name='wo'),
    path('price', views.priceO, name='priceO'),
    path('active', views.activeO, name='activeO'),
    path('canceled', views.canceledO, name='canceledO'),
    path('waitOh', views.waitOh, name='waitOh'),
    path('dpo', views.DpO, name='dpo'),
    path('done', views.DoneO, name='doneO'),
]
