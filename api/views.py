from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import CoreJSONRenderer
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from .permissions import IsOwner
from api import models
from django.contrib.auth.models import User
from api import serializers

# Create your views here.


# CBF
# class Process(APIView):
#     """
#     List all processes, or create a new process.
#     """
#     def get(self, request, format=None):
#         processes = Process.objects.all()
#         serializer = ProcessSerializer(processes, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProcessSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = SchemaGenerator(title='Rasterbucket process API')
    return Response(generator.get_schema(request=request))


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, IsOwner, ))
def process_list(request):
    if request.method == 'GET':
        processes = models.Process.objects.all()
        serializer = serializers.ProcessSerializer(processes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ProcessSerializer(data=request.data)
        if serializer.is_valid():  # TODO add more validation
        # see https://richardtier.com/2014/03/24/json-schema-validation-with-django-rest-framework/
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.IsAuthenticated, IsOwner, ))
def process_detail(request, id):
    process = get_object_or_404(models.Process, pk=id)

    if request.method == 'GET':
        serializer = serializers.ProcessSerializer(process)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ProcessSerializer(process, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        process.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RasterbucketCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api"""
    queryset = models.Rasterbucket.objects.all()
    serializer_class = serializers.RasterbucketSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new rasterbucket."""
        serializer.save(owner=self.request.user)


class RasterbucketDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE request
        view with Read, Update and Delete"""
    queryset = models.Rasterbucket.objects.all()
    serializer_class = serializers.RasterbucketSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)


class RasterbucketServiceCreateView(generics.ListCreateAPIView):
    """Defines the rasterbucket service creation behavior"""
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
    queryset = models.RasterbucketService.objects.all()
    serializer_class = serializers.RasterbucketServiceSerializer

    def perform_create(self, serializer):
        """"""
        pk = self.kwargs.get('pk_bucket')
        rasterbucket = get_object_or_404(
            models.Rasterbucket,
            pk=pk,
            owner=self.request.user)
        serializer.save(
            rasterbucket=rasterbucket,
            owner=self.request.user)


class RasterbucketServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Defines an actionable rasterbucket service view
       with Read, Update and Delete"""
    queryset = models.RasterbucketService
    serializer_class = serializers.RasterbucketServiceSerializer

    def get_object(self):
        """specifies the object used for `update`,
         `retrieve`, `destroy` actions"""
        return get_object_or_404(
            models.RasterbucketService,
            pk=self.kwargs.get('pk_service'))


class MapServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Defines an actionable map service view
       with Read, Update and Delete"""
    queryset = models.BaseServiceModel
    serializer_class = serializers.MapServiceSerializer

    def get_object(self):
        """specifies the object used for `update`,
         `retrieve`, `destroy` actions"""
        return get_object_or_404(
            models.BaseServiceModel,
            pk=self.kwargs.get('pk_map'))


class GEEMapServiceCreateView(generics.ListCreateAPIView):
    """Defines the GEE map service creation behavior"""
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
    queryset = models.GEEMapService.objects.all()
    serializer_class = serializers.GEEMapServiceSerializer

    def perform_create(self, serializer):
        """"""
        pk = self.kwargs.get('pk_service')
        rasterbucketservice = get_object_or_404(
            models.RasterbucketService,
            pk=pk,
            owner=self.request.user)
        serializer.save(
            rasterbucketservice=rasterbucketservice,
            owner=self.request.user)


class GEEMapServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Defines an actionable GEE map service view
       with Read, Update and Delete"""
    queryset = models.GEEMapService
    serializer_class = serializers.GEEMapServiceSerializer

    def get_object(self):
        """specifies the object used for `update`,
         `retrieve`, `destroy` actions"""
        return get_object_or_404(
            models.GEEMapService,
            pk=self.kwargs.get('pk_map'))


class TileMapServiceCreateView(generics.ListCreateAPIView):
    """Defines the Tile map service creation behavior"""
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
    queryset = models.TileMapService.objects.all()
    serializer_class = serializers.TileMapServiceSerializer

    def perform_create(self, serializer):
        """"""
        pk = self.kwargs.get('pk_service')
        rasterbucketservice = get_object_or_404(
            models.RasterbucketService,
            pk=pk,
            owner=self.request.user)
        serializer.save(
            rasterbucketservice=rasterbucketservice,
            owner=self.request.user)


class TileMapServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Defines an actionable Tile map service view
       with Read, Update and Delete"""
    queryset = models.TileMapService
    serializer_class = serializers.TileMapServiceSerializer

    def get_object(self):
        """specifies the object used for `update`,
         `retrieve`, `destroy` actions"""
        return get_object_or_404(
            models.TileMapService,
            pk=self.kwargs.get('pk_map'))


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
