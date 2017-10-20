from django.shortcuts import render, HttpResponse


def post_index(request):
    return HttpResponse('Burası Post index Sayfası !')


def post_detail(request):
    return HttpResponse('Burası Post detail Sayfası !')


def post_create(request):
    return HttpResponse('Burası Post create Sayfası !')


def post_update(request):
    return HttpResponse('Burası Post update Sayfası !')


def post_delete(request):
    return HttpResponse('Burası Post delete Sayfası !')