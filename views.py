from django.http import JsonResponse
import json
import os


def rest_content(request):
    with open(os.path.join(os.getcwd(), 'dummyapp', 'tivol_migrations', 'source_files', 'filmmakers.json'), 'r') as file:
        return JsonResponse(json.load(file), safe=False)
