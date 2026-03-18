from django.urls import path
# from main_app.views import [function name]
from main_app import views


urlpatterns = [
   path('transaction_function/', views.transaction_function),
   path('transaction/', views.TransactionAPI.as_view())
]

