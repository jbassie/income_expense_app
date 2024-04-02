from django.urls import path 
from . import views


urlpatterns = [
     path('expense_edit/<int:id>', views.expense_edit, name="expense_edit"),
     path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('', views.index, name="expenses"),
    path('add-expense/', views.add_expense, name='add-expenses'),
   
]
