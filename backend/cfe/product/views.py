from rest_framework import generics

from . models import Product
from .serializers import ProductSerializers

class ProductCreateAPIView(generics.CreateAPIView):
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

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # lookup_field = 'pk'