from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


#Serializers 
from . import serializers
from rest_framework import status


#profile
from . import models

#PERMISSIONS 
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

#status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


#Login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# VIEWSET
from rest_framework import viewsets

# Create your views here.


class HelloApiView(APIView):
	"""test api"""

	serializer_class = serializers.HelloSerializer	

	def get(self,request, format = None):
		"""resturn a list of api features. """
		an_apiview = [
			'use Htp (get, post, patch, put, delet',
			'it is similar to a traditional Django view',
			'give you the most control over your logic',
			'is mapped manually to urls'

		]

		return Response({'message ': 'Hello', 'an_apiview': an_apiview})

	def post(self,request):
		"""create a hello message with our name """

		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'hello {0}'.format(name)
			return Response({'message':message})
		else :
			return Response(
				serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def put(self,request, pk = None):

		"""handeling updating

		pk is primary key this is for hadneling data	"""
		return Response({'method':'put'})


	def patch(self,request, pk=None):
		""" for updating data"""
		return Response({'method':'patch'})

	def delete(self, response, pk=None):

		"""delet an object"""

		return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
	"""Test ViewsSet"""
	

	serializer_class = serializers.HelloSerializer

	def list(self,request):
		""" Return a hello message """

		a_viewset = [
			'use parial',
			'automaticly user urls',
			'provides more fucnationaly with less code',
		]

		return Response({'message':'Hello','a_viewset':a_viewset})


	def create(self,request):

		"""Create a new hello messgae"""

		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'hello {0}'.format(name)
			return Response({'message':message})

		else: 
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )


	def retrieve(self,request,pk =None):

		"""handeles getting an object"""

		return Response({'http_method':'GET'})


	def update(self, request, pk=None):
		"""pk none because we want to know wich objecting is updating"""
		return Response({'http_method':'PUT'})	

	def partial_update(self,request,pk=None):

		"""Handles updating part of an object"""

		return  Response({'http_method':'PATCH'})

	def destroy(self, request, pk=None):

		"""handels removing"""

		return Response({'http_method':'DELETE'})


'''
class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handels creating and updating profiles"""
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.object.all()

	#permission_classes = (permissions.UpdateOwnProfile,)

	authentication_classes = (TokenAuthentication,)

	#authentication_class = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

'''





class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    seach_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):

	""" check email and etc"""

	serializer_class = AuthTokenSerializer
	def create(self,request):

		""" use the obtain the apiview to validate token"""
		return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
	authentication_classes = (TokenAuthentication,)
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all()
	permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
	def perform_create(self,serializer):
		"""setd the user loged in user"""
		serializer.save(user_profile=self.request.user)


















