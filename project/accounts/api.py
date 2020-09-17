from rest_framework.response import Response
from rest_framework.decorators import api_view
from .seralizers import ProfileSerializer
from .models import Profile
from rest_framework import generics


@api_view(['GET'])
def profiles(request):
    profile = Profile.objects.all()
    data = ProfileSerializer(profile, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def profiles_id(request, id):
    profile_id = Profile.objects.get(id=id)
    data = ProfileSerializer(profile_id).data
    return Response({'data': data})


class Profile_Api(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class Profile_Api1(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class Profile_Api2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
