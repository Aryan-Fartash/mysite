from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def http_response(request):
    return HttpResponse('this is a http test dude')

def json_response(request):
    return JsonResponse({'Description':'this is a json test dude','ps':'Im the God'})

