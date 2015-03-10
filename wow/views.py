# -*- coding: utf-8 -*-
"""

"""
from django.http.response import HttpResponse, Http404
from django.template import Context, Template


def test_view(request):

    return HttpResponse(content='This is a test', content_type='text/plain')


def test_view_2(request):

    return HttpResponse(content='This is another test', content_type='text/plain')


def template_loader_view(request, template):
    if not isinstance(template, Template):
        raise Http404()

    html = template.render(Context())
    return HttpResponse(html)