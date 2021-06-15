from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import UserSerializer, MutualSerializer, StocksSerializer, CompanyStocksSerializer, CompanyMutualSerializer, CompanyGoldSerializer, GoldSerializer
from .models import User, Mutual, Stocks, CompanyStocks, CompanyMutual, CompanyGold, Gold
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = User.objects.get(id=id)
            serializer = UserSerializer(stu)
            return Response(serializer.data)
        stu = User.objects.all()
        serializer = UserSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = User.objects.get(id=id)
        serializer = UserSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = User.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})


# user stocks
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def stocks_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Stocks.objects.get(id=id)
            serializer = StocksSerializer(stu)
            return Response(serializer.data)
        stu = Stocks.objects.all()
        serializer = StocksSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StocksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Stocks.objects.get(id=id)
        serializer = StocksSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Stocks.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})


# user mutual
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def mutual_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Mutual.objects.get(id=id)
            serializer = MutualSerializer(stu)
            return Response(serializer.data)
        stu = Mutual.objects.all()
        serializer = MutualSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MutualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Mutual.objects.get(id=id)
        serializer = MutualSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Mutual.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})

# user gold


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gold_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Gold.objects.get(id=id)
            serializer = GoldSerializer(stu)
            return Response(serializer.data)
        stu = Gold.objects.all()
        serializer = GoldSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GoldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Gold.objects.get(id=id)
        serializer = GoldSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Gold.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})


# company stocks
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def company_stocks_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = CompanyStocks.objects.get(id=id)
            serializer = CompanyStocksSerializer(stu)
            return Response(serializer.data)
        stu = CompanyStocks.objects.all()
        serializer = CompanyStocksSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CompanyStocksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = CompanyStocks.objects.get(id=id)
        serializer = CompanyStocksSerializer(
            stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = CompanyStocks.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})


# comapny mutual
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def company_mutual_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = CompanyMutual.objects.get(id=id)
            serializer = CompanyMutualSerializer(stu)
            return Response(serializer.data)
        stu = CompanyMutual.objects.all()
        serializer = CompanyMutualSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CompanyMutualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = CompanyMutual.objects.get(id=id)
        serializer = CompanyMutualSerializer(
            stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = CompanyMutual.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})
# company gold


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def company_gold_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = CompanyGold.objects.get(id=id)
            serializer = CompanyGoldSerializer(stu)
            return Response(serializer.data)
        stu = CompanyGold.objects.all()
        serializer = CompanyGoldSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CompanyGoldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data posted"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = CompanyGold.objects.get(id=id)
        serializer = CompanyGoldSerializer(
            stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data updated"})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = CompanyGold.objects.get(id=id)
        stu.delete()
        return Response({'msg': "Data deleted"})


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class MutualViewSet(viewsets.ModelViewSet):
#     queryset = Mutual.objects.all()
#     serializer_class = StocksSerializer
# class StocksViewSet(viewsets.ModelViewSet):
#     queryset = Stocks.objects.all()
#     serializer_class = StocksSerializer
# class CompanyStocksViewSet(viewsets.ModelViewSet):
#     queryset = CompanyStocks.objects.all()
#     serializer_class = CompanyStocksSerializer
