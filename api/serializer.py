from rest_framework import serializers
from api.models import Expense, Category1

class Category1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = (
            'id',
            'name'
        )

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'description',
            'amount',
            'category',

            'payment_date',
            'created_on',
            'last_modified',
            'method_payment'
        )
