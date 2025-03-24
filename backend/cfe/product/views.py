from rest_framework import generics
from rest_framework.decorators import api_view

from . models import Product
from .serializers import ProductSerializers
from django.shortcuts import get_object_or_404
from django.http import Http404

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
    # lookup_field = 'pk'
    
@api_view(['GET', 'POST']) 
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
        pass
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(serializer.data)
        return Response({"invalid" : "not good data"}, status=500)