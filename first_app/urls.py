from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('logup/',views.logup,name='logup'),
    path('singout/',views.singout,name='singout'),
    path('search/<user>/',views.search,name='search'),
    path('home/<user>/',views.home,name='home'),
    path('songSerch/<user>',views.songSerch,name='songSerch'),
    path('analysis/<user>',views.analysis,name='analysis'),

    path('scoreone/<user>-<dataRes>',views.scoreone,name='scoreone'),
    path('scoretwo/<user>-<dataRes>',views.scoretwo,name='scoretwo'),
    path('scorethree/<user>-<dataRes>',views.scorethree,name='scorethree'),
    path('scorefour/<user>-<dataRes>',views.scorefour,name='scorefour'),
    path('scorefive/<user>-<dataRes>',views.scorefive,name='scorefive'),
]
