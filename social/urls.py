# urls.py

from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='home'),
    path('reply/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('like/', views.like_message, name='like_message'),
    path('create_message/', views.create_message, name='create_message'),
]