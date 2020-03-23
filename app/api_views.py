from . import models
from . import serializers

from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import parsers, renderers, status, viewsets
from rest_framework.decorators import action, api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Appication.objects.all()
    serializer_class = serializers.ApplicationSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser,
                      parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    http_method_names = ['get',]
    lookup_field = 'api_key'

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.Appication.objects.all()
    serializer_class = serializers.ApplicationSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser,
                      parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated],
            url_path='change_key', url_name='change_key')
    def change_key(self, request, pk=None):
        app = get_object_or_404(models.Appication, pk=pk)
        app.api_key = app.generate_api_key()
        app.save()
        serializer = self.serializer_class(app)
        return Response(serializer.data)
        

