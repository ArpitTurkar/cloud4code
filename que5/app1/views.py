from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data=request.data)
  
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_product(request):
    
    if request.query_params:
        product = Product.objects.filter(**request.query_param.dict())
    else:
        product = Product.objects.all()
  
    if product:
        data = ProductSerializer(product, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(instance=product, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_202_ACCEPTED)