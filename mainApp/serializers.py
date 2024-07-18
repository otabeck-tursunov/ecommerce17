from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # subCategory = SubCategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        product = super(ProductSerializer, self).to_representation(instance)

        images = Image.objects.filter(product=instance)
        images_serializer = ImageSerializer(images, many=True)

        _important_properties = Property.objects.filter(important=True, product=instance)
        important_properties = {}
        for p in _important_properties:
            if p.name in important_properties.keys():
                important_properties.update(
                    {
                        p.name: important_properties.get(p.name) + [
                            {
                                'id': p.id,
                                'value': p.value,
                            }
                        ]
                    }
                )
            else:
                important_properties.update(
                    {
                        p.name: [
                            {
                                'id': p.id,
                                'value': p.value,
                            }
                        ]
                    }
                )

        basic_properties = Property.objects.filter(important=False, product=instance)

        basic_properties_serializer = PropertySerializer(basic_properties, many=True)

        product.update(
            {
                'images': images_serializer.data,
                'important_properties': important_properties,
                'basic_properties': basic_properties_serializer.data
            }
        )
        return product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'name', 'value')

        def validate(self, data):
            if not data.get('important') and data.get('name') not in Property.objects.filter(
                    product=data.get('product'), important=False).values('name', flat=True):
                raise serializers.ValidationError('Property already exists!')
            return data
