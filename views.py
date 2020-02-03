from django.http import HttpResponse
from django.shortcuts import render


def rest_content(request):
    html = "<html><body>It is now %s.</body></html>"
    return HttpResponse(html)
