import json
from django.http import Http404, HttpResponse

from project_litter_bug_web.service import retrieve_life_stats


def aggregate_data_handler(request):
    if request.is_ajax() and request.method == 'GET':
        aggregate = retrieve_life_stats()
        data = json.dumps(aggregate)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

