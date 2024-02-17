from django.urls import path
from . import views

urlpatterns =[
    path('',views.post_list, name='post_list'),
    path('',views.Voetbalspeler_list, name='post_list'),
    path('',views.wielrenner_list, name='wielrenner_list'),

]