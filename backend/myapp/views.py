from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer


def menu_page(request):
    categories = Category.objects.prefetch_related(
        'subcategories__products'
    ).order_by('sort_order')
    context = {
        'categories': categories
    }
    return render(request, 'menu/menu_page.html', context)


@api_view(['GET'])
def menu_view(request):
    categories = Category.objects.prefetch_related(
        'subcategories__products'
    ).order_by('sort_order')

    serializer = CategorySerializer(categories, many=True, context={'request': request})
    return Response(serializer.data)
