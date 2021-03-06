from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of API View features """

        an_apiviem = [
            'Uses HTTP method',
            'Its similar to a traditional Django',
            'Its mapped manually'
        ]

        return Response({'message': 'Hello', 'an_api': an_apiviem})

    def post(self, request):
        """ Create hello message with name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk is primary key
    def put(self, request, pk=None):
        """ Update objects"""

        return Response({'method': 'put'})

    # pk is primary key
    def patch(self, request, pk=None):
        """ Patch - Partial Update objects"""

        return Response({'method': 'patch'})

    # pk is primary key
    def delete(self, request, pk=None):
        """ Delete objects"""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return hello message """
        a_viewset = [
            'Uses actions (list,create,retrieve,update, partial_update)',
            'Automatically maps to Routers',
            ' Less Code'
        ]
        return Response({'message': 'Hello!', 'viewset': a_viewset})

    def create(self, request):
        """ Create a new Hello Message """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk is primary key
    def retrieve(self, request, pk=None):
        """ GET objects"""

        return Response({'method': 'GET'})

    # pk is primary key
    def update(self, request, pk=None):
        """ Update objects"""

        return Response({'method': 'PUT'})

    # pk is primary key
    def partial_update(self, request, pk=None):
        """ Patch - Partial Update objects"""

        return Response({'method': 'patch'})

    # pk is primary key
    def destroy(self, request, pk=None):
        """ Delete objects"""

        return Response({'method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, update"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """ checks e-mail and password """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """" User the ObtainAuthToken AOI View to validate and create a token """

        return ObtainAuthToken().post(request)