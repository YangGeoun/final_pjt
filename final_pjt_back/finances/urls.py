from django.urls import path
from . import views

urlpatterns = [
    path('getdeposit/', views.getdeposit),
    path('deposit/', views.deposit),
    path('deposit/join/', views.deposit_join),
    path('do/', views.getdeopsitoption),
    path('getsaving/', views.getsaving),
    path('saving/', views.saving),
    path('saving/join/', views.saving_join),
    path('so/', views.getsavingoption),
    path('getcard/', views.getcard),
    path('card/', views.card),
    path('cardsearch/<conditions>/', views.cardsearch),
    path('cardrecommend/', views.cardrecommend),
    path('fund/', views.getfund),
    path('test/', views.test),
    path('searchdeposit/<bank>/<type>/<term>/', views.search_deposit),
    path('searchsaving/<bank>/<type>/<term>/', views.search_saving),
    path('recommend/', views.recommend),

]
