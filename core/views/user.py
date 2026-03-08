from django.http import HttpResponse
from django.shortcuts import render


def user(request, uid):
    return HttpResponse(f"User id: {uid}")
