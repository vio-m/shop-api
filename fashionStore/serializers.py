from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('__all__')

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['size']

class ProductSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='size'
    )
    class Meta:
        model = Product
        fields = ['id', 'size', 'name', 'description', 'brand', 'category',
                  'price', 'image', 'date', 'sale', 'size', 'tag', 'percent']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')