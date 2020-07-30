from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DownExpSerializer, UpExpSerializer, AnnotationSerializer
from .models import DownExp, UpExp, Annotations
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers

# Create your views here.


class DownExpViewset(viewsets.ModelViewSet):
    serializer_class = DownExpSerializer
    queryset = DownExp.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['gene']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        downexp = self.get_object()
        return Response(downexp.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpExpViewset(viewsets.ModelViewSet):
    serializer_class = UpExpSerializer
    queryset = UpExp.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['gene']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        upexp = self.get_object()
        return Response(upexp.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AnnotationViewset(viewsets.ModelViewSet):
    serializer_class = AnnotationSerializer
    queryset = Annotations.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['gene']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        annot = self.get_object()
        return Response(annot.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)