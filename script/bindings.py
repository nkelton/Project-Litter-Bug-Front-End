from channels_api.bindings import ResourceBinding

from .models import Script
from .serializers import ScriptSerializer


class ScriptBinding(ResourceBinding):

    model = Script
    stream = "script"
    serializer_class = ScriptSerializer
    queryset = Script.objects.get(pk=1)
