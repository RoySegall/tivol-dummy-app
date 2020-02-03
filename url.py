from django.urls import path
from dummyapp.views import rest_content

urlpatterns = [
    path('/rest', rest_content, name='dummy_rest_content'),
]
