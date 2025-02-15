from django.shortcuts import render

from django.http import JsonResponse
from school_management.elasticsearch_client import es


def search_view(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size', 10))
    from_ = (page - 1) * size
    # TODO: apply staff and guardians permissions
    response = es.search(index="homework", body={
        "query": {
            "query_string": {
                "query": f"*{query}*",
                "fields": ["title", "description"]
            }
        },
        "from": from_,
        "size": size
    })
    return JsonResponse(response.body['hits'], safe=False)
