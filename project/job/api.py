from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Job
from .seralizers import JobSerializer
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def job_detail_api(request, id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data': data})


class Job_List_Api(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Job_List_Api1(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Job_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
