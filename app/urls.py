from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryManagementView.as_view(), name = 'category'),
    path('category/<int:id>/', CategoryEditManagementView.as_view(), name = 'category_edit'),
    path('transaction/', TransactionManagementView.as_view(), name = 'transaction'),
    path('transaction/<int:id>/', TransactionEditManagementView.as_view(), name = 'transaction_edit'),
]