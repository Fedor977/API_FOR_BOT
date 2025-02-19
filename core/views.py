from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


@api_view(['GET'])
def category_list(request):
    """ Получить список всех категорий """
    if request.method == 'GET':
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True,
                                        context={'request': request})
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def products_category(request, category_id):
    """ Получить список продуктов по конкретной категории """
    if request.method == 'GET':
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)

        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True,
                                       context={'request': request})
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)
