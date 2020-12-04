from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


from .models import Job, JobReply, Resume
from .permissions import JobPermission
from .serializers import JobSerializer, JobDetailsSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobDetailsSerializer
    filterset_backends = [DjangoFilterBackend, ]
    filter_fields = ['categories', ]
    search_fields = ['title', ]


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     params = self.request.query_params
    #
    #     print(params)
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [JobPermission, ]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return JobSerializer
        return JobDetailsSerializer

    def get_serializer_context(self):
        return {'action': self.action}

    # @action(detail=True, methods=['post'])
    # def reply(self, request, pk=None):
    #     job = self.get_object()
    #     JobReply.objects.create(job=job, resume=request.user.resume)


# class CreateAPIView(ModelViewSet):
#     queryset = Resume.objects