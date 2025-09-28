from django.urls import path
from . import views

urlpatterns = [
     path('trades/', views.trade_list),  # New Trade API
]
