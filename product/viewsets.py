from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"

# we can use this instead of the normal api urls because they support all api methods 
#get |post |put |patch |delete