from .models import User, Stocks, Mutual,CompanyStocks,CompanyMutual,CompanyGold,Gold
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'useremail', 'balance']


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['id', 'user', 'company', 'quantity', 'prices']


class MutualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutual
        fields = ['id', 'user', 'company', 'quantity', 'prices']


class GoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gold
        fields = ['id', 'user', 'company', 'quantity', 'prices']


class CompanyStocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStocks
        fields = ['id', 'Name', 'quantity']


class CompanyMutualSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMutual
        fields = ['id', 'Name', 'quantity']


class CompanyGoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGold
        fields = ['id', 'Name', 'quantity']
