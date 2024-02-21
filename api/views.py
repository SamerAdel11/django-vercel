from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from product.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.serializers import ProductSerializer

# Create your views here.
@api_view(['GET','POST'])
def api(request,*args,**kwargs):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print("Valid")
        # serializer.save()
        return Response(serializer.data)
    else:
        print('invalid')
        return HttpResponse("There is an error")
        # elif request.method=="GET":


def hello(request):
    return HttpResponse("Hello world")

    # print(request.GET) # url query parameters
    # body=request.body # string of json data
    # data={}
    # try:
    #     # the json data that has been passed with that request
    #     data=json.loads(body) #string of json data --> python dict
    # except:
    #     pass
    # data['params']=request.GET
    # data['content_type']=request.content_type
    # print(data.keys())
    # print("*"*100)
