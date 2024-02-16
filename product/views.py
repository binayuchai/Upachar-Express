from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from product.models import *
from product.serializers import *

class ProductListView(APIView):
    # List all product
    
    def get(self,request,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    # def post(self,request,format=None):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductByCategoryView(APIView):
    # List product by category
    def get(self,request,category_slug,format=None):
        try:
            category = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

            
        print("Checking of category",category)
        products = category.products.all()
        print("Result of products: ",products)
        print(products)
        
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
class ProductRegisterView(APIView):
    def post(self,request,format=None):
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
class ProductDetailView(APIView):
    def get(self,request,category_slug,product_slug):
        
        product = get_object_or_404(Product,category__slug=category_slug,slug=product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
