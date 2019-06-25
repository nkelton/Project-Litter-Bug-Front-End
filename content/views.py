from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers


class ContentRetrieveAndDelete(APIView):
    def get_object(self, litter_id):
        try:
            return models.Content.objects.filter(litter_id=litter_id)
        except:
            raise Http404

    def get(self, request, litter_id, format=None):
        results = self.get_object(litter_id)
        content = []
        print(request.data)

        for result in results:
            serialized_data = serializers.ContentSerializer(result)
            content.append(serialized_data.data)
        return Response(content)

    def delete(self, request, litter_id, format=None):
        results = self.get_object(litter_id)

        for result in results:
            result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentList(generics.ListCreateAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer
