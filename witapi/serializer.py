from rest_framework import serializers
from witapi.models import Expense, Category, Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'name'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'description',
            'author',
            'amount',
            'category',
            'payment',
            'payment_date',
            'created_on',
            'last_modified'

        )
