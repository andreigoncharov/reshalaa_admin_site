from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ppp'),
    #path('active', views.activeO, name='activeO'),
    #path('canceled', views.canceledO, name='canceledO'),
    #path('wait', views.waitO, name='waitO'),
    #path('done', views.doneO, name='doneO'),
]
