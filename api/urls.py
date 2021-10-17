from django.urls import path
from . import views
from .views import Category1List,Category1Detail

urlpatterns =[
    path('', views.apiOverview,name="api-overview"),
    path('categories-list', Category1List.as_view(), name="categories-list"),
    path('categorie-detail/<str:pk>/', Category1Detail.as_view(), name="categories-detail"),
    path('expense-list', views.expenseList, name="expense-list"),

    path('expense-detail/<str:pk>/', views.expenseDetail, name="expense-detail"),
    path('expense-create/', views.expenseCreate, name="expense-create"),
    path('expense-update/<str:pk>/', views.expenseUpdate, name="expense-update"),
    path('expense-delete/<str:pk>/', views.expenseDelete, name="expense-delete"),
]
