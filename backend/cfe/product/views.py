from rest_framework import generics, mixins
from rest_framework.decorators import api_view

from . models import Product
from .serializers import ProductSerializers
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response

class ProductMixinView(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validate_data-get('title')
        content = serializer.validated_data-get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
            
        print(serializer)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = intance.title
            
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# @api_view(['GET', 'POST']) 
def product_alt_view(request, pk=None, *args, **kwargs):
    
    method = request.method
    
    if method == "GET":
        if pk is not None:
        # get request -> detail view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=false).data
            return Response(data)
    
    # list view 
        queryset = Product.objets.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        # pass
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(serializer.data)
        return Response({"invalid" : "not good data"}, status=500)