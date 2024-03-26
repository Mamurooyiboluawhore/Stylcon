from rest_framework import serializers
from .models import Catalogue


class CatalogueSerializers(serializers.ModelSerializer):
    class meta:
        model = Catalogue
        field = '__all__'