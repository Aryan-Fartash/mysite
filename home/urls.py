from django.urls import path
from home.views import http_response,json_response

urlpatterns = [
    path('http_test',http_response),
    path('json_test',json_response)
]