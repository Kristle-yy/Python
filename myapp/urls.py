from django.urls import path
from . views import info_list, info_create

urlpatterns = [
    path('infolist/', info_list, name='info_list'),
    path('infolist/create/', info_create, name='info_create'),
]
