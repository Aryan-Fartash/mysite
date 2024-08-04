from django.urls import path,include
from website.views import response

urlpatterns = [
    path('server_test', response),
    path('home/',include('home.urls'))
]