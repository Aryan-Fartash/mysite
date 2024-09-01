from django.urls import path,include
from blog.views import blog_view,blog_single

app_name='blog'

urlpatterns = [
    path('', blog_view , name='index' ),
    path('/single', blog_single , name='single'),
]