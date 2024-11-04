from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ListLinksSerializer
from rest_framework.response import Response
from .scrapy import find_links



# Create your views here.

class ListLinks(APIView):
    def get(self, request, format=None):
        links = find_links()
        serializer = ListLinksSerializer(links, many=True)
        print(serializer.data)
        return Response(serializer.data)

class RewieLink(APIView):
    def get(self,request,pk, format=None):
        links = find_links()
        element = [el if el['id'] == pk else None for el in links][0]
        if element:
            serializer = ListLinksSerializer(element)
            return Response(serializer.data)
        else:
            return Response({'message':'stop'})





