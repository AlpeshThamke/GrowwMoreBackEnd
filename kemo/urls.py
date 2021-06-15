"""kemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('user', views.UserViewSet, basename='user')
# router.register('mutual', views.MutualViewSet, basename='mutual')
# router.register('stocks', views.StocksViewSet, basename='stocks')
# router.register('companystocks', views.CompanyStocksViewSet, basename='Company_Stocks')


urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('userapi/', views.user_api),
    path('goldapi/', views.gold_api),
    path('mutualapi/', views.mutual_api),
    path('stocksapi/', views.stocks_api),
    path('companystocksapi/', views.company_stocks_api),
    path('companymutualapi/', views.company_mutual_api),
    path('companygoldapi/', views.company_gold_api),

    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
