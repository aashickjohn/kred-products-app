from rest_framework import serializers
from oshop.models import Product, Orders

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'prod_name', 'prod_price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'prod_name', 'buyer_id_id', 'buy_quantity']