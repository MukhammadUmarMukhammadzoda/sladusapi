from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def update(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('O`chirildi!')