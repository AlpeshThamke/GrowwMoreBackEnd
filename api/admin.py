from django.contrib import admin
from .models import User, Stocks, Mutual,Gold,CompanyStocks,CompanyGold,CompanyMutual
# Register your models here.

# for users
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'useremail', 'balance']


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'quantity', 'prices']


@admin.register(Mutual)
class MutualAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'quantity', 'prices']


@admin.register(Gold)
class GoldAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'quantity', 'prices']



# for companies 
@admin.register(CompanyStocks)
class CompanyStocksAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'quantity']


@admin.register(CompanyMutual)
class CompanyMutualAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'quantity']


@admin.register(CompanyGold)
class CompanyGoldAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'quantity']
