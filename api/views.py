from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import  permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializer import  ExpenseSerializer, Category1Serializer

from .models import Expense, Category1
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/expense-list/',
        'Listcat':'/categories-list/',
        'Detail View ':'/expense-detail/<str:pk>/',
        'Detail View cat':'/categorie-detail/<str:pk>/',

        'Create':'/expense-create/',
        'Update':'/expense-update/<str:pk>/',
        'Delete':'/expense-delete/<str:pk>/',

    }
    return Response(api_urls)

@api_view(['GET'])
def expenseList(request):
    expenses =Expense.objects.all()

    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def expenseDetail(request, pk):
        expenses = Expense.objects.get(id=pk)

        serializer = ExpenseSerializer(expenses, many=False)
        return Response(serializer.data)

@api_view(['POST'])
def expenseCreate(request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



@api_view(['POST'])
def expenseUpdate(request, pk):
        expense = Expense.objects.get(id=pk)
        serializer = ExpenseSerializer(instance=expense, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

@api_view(['Delete'])

def expenseDelete(request, pk):
    
    expense = Expense.objects.get(id=pk)

    expense.delete()

    return Response("expense successfully delete!")




class Category1List(generics.ListCreateAPIView):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class Category1Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                         #IsOwnerOrReadOnly]
