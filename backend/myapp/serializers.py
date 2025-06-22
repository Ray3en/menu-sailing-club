from rest_framework import serializers
from .models import Category, Subcategory, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'is_available']


class SubcategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'products']

    def get_products(self, obj):
        products = obj.products.filter(is_available=True).order_by('sort_order')
        return ProductSerializer(products, many=True, context=self.context).data


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'slug', 'subcategories']

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all().order_by('sort_order')
        return SubcategorySerializer(subcategories, many=True, context=self.context).data
