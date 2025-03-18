import json
from django.http import JsonResponse, HttpResponse
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializers

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    
    data1 = request.data
    serializer = ProductSerializers(data=data1)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)
        instance = serializer.save()
        print(instance)
        data = serializer.data
        return Response(serializer.data)
    # instance = Product.objects.all().order_by("?").first()
    # data = ProductSerializers(instance).data
    # data = {}
    # print("yes")
    # if instance:
    #     data = ProductSerializers(instance).data
    # return Response(data)

    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    # return Response(data)
    # return JsonResponse(data)
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # return JsonResponse(data)
    
# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
    
#     # data = request.data
#     data = ProductSerializers(data=request.data)
#     print(data)
#     return Response(data.data)
#     # serializer = ProductSerializers(data=data)

#     # if serializer.is_valid():
#         # print(serializer.data)
#         # data = serializer.data/
#         # return Response(data)
#     # return Response(serializer.data)
