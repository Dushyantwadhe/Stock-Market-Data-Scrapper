from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create_cards/', views.create_cards, name='create_cards'),
    # path('cards_val/', views.cards_val, name='cards_val')
]
