from django.urls import path 
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
     path('expense_edit/<int:id>', views.expense_edit, name="expense_edit"),
     path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('', views.index, name="expenses"),
    path('add-expense/', views.add_expense, name='add-expenses'),
    path("search-expenses", csrf_exempt(views.search_expenses), name="search-expenses")

]
