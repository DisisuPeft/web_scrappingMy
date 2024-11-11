from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from .search_service import search_products_links, prices_products
from rest_framework.response import Response
from .models import URLs
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import URLsSerializer


# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_products_view(request):
    term = request.data.get('search_term')
    # print(request.data['search_term'], request.method)
    if not term:
        return Response({'error': 'Please enter search term'}, status=status.HTTP_400_BAD_REQUEST)
    #
    links = search_products_links(term)
    urls_to_create = []  # Lista para almacenar los objetos URLs sin guardar
    #
    for link in links:
        urls_to_create.append(URLs(url=link, article=term))

    # Guardar todos los objetos en la base de datos de una vez
    created_urls = URLs.objects.bulk_create(urls_to_create)
    #
    # # Serializar los objetos creados para devolverlos en la respuesta
    serializer = URLsSerializer(created_urls, many=True)

    urls = URLs.objects.filter(article=term)
    price = prices_products(list(urls.values()))
    print(price)
    return Response({'links': list(urls.values())}, status=status.HTTP_200_OK)
# def create_products_view(request):
#     term = request.data['search_tearm']
#     # print(request.content_type)
#     # serializer = URLsSerializer(data=request.data)
#     if not term:
#         return Response({'error': 'Please enter search term'}, status=status.HTTP_400_BAD_REQUEST)
#
#     links = search_products_links(term)
#     for link in links:
#         serializer = URLsSerializer(data={'url': link, 'article': term})
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     links_exists = URLs.objects.all()
#     return Response({'links': links_exists}, status=status.HTTP_200_OK)
    # creo que esta parte se trabajara para cuando existan mas datos, para asi llevar un conteo de cuanto ya existe y aca entraria el machine learning
    # if links_exists is not None:
    #     for links_exist in links_exists:
    #         if links_exist.url in links:
    #
    # for link in links:
    #     serializer.save(url=link, article=term)
    # links_exists = URLs.objects.all()
    #
    # return Response({'links': links_exists}, status=status.HTTP_200_OK)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)