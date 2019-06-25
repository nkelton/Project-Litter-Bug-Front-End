from channels_api.bindings import ResourceBinding

from .models import Content
from .serializers import ContentSerializer


class ContentBinding(ResourceBinding):
    model = Content
    stream = "content"
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
