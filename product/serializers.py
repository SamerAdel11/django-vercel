from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ 
    if we need to change the name of key that will result in the api itself
    (other name than that exist in the model)
    so we have to use method SerializerMethodField()
    which will wait for a function called get_NewVariableName
    and what will be returned in this function will be the value for that variable
    """
    Difference = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product_description")

    class Meta:
        model = Product
        fields = ["id", "url",  "title",
                  'content', 'price', 'sale_price', 'Difference']

    def get_Difference(self, obj):
        # this condition will be used when ww don't save the data passed throught the api
        # so that there is no instance attached to the serializer
        if not isinstance(obj, Product):
            return None
        else:
            return obj.discount_diff()
