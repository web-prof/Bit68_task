from rest_framework.decorators import APIView, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import Products_serializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.contrib.auth.models import User


class get_post_products(APIView):
    queryset = Products.objects.all()
    model = Products
    # permission_classes=[IsAuthenticated]

    def get(self, request):
        params = self.request.query_params.get('search', None)
        if params:
            qs = Products.objects.filter(
                prd_owner__username__startswith=params)
        else:
            qs = Products.objects.all()
        Products_ser = Products_serializer(qs, many=True)
        return Response(Products_ser.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        product_ser = Products_serializer(data=request.data)
        if product_ser.is_valid():
            user = User.objects.get(username=request.data['prd_owner'])
            product_ser.save(prd_owner=user)
            return Response(product_ser.data, status=status.HTTP_201_CREATED)
        return Response(product_ser.errors, status=status.HTTP_400_BAD_REQUEST)


class get_update_delete_product(APIView):
    # permission_classes=[IsAuthenticated]
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        products_ser = Products_serializer(product)
        return Response(products_ser.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        products_ser = Products_serializer(product, data=request.data)
        if products_ser.is_valid():
            products_ser.save()
            return Response(products_ser.data)
        return Response(products_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
