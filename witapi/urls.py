from django.urls import path
from . import views
from .views import CategoryList,CategoryDetail,PaymentList,PaymentDetail

urlpatterns =[
    path('', views.apiOverview,name="api-overview"),
    path('categories-list', CategoryList.as_view(), name="categories-list"),
    path('categorie-detail/<str:pk>/', CategoryDetail.as_view(), name="categories-detail"),

    path('payment-list', PaymentList.as_view(), name="payment-list"),
    path('payment-detail/<str:pk>/', PaymentDetail.as_view(), name="payment-detail"),

    path('expense-list', views.expenseList, name="expense-list"),

    path('expense-detail/<str:pk>/', views.expenseDetail, name="expense-detail"),
    path('expense-create/', views.expenseCreate, name="expense-create"),
    path('expense-update/<str:pk>/', views.expenseUpdate, name="expense-update"),
    path('expense-delete/<str:pk>/', views.expenseDelete, name="expense-delete"),
]
