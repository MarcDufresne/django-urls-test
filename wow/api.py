# -*- coding: utf-8 -*-
"""

"""
from django.conf.urls import patterns, url
from django.template.loader import get_template_from_string
from django.views.generic.base import RedirectView
from wow.models import URLTest, URLToTemplate, URLRedirect


def test_load_url(my_patterns):

    urls = URLTest.objects.all()

    for my_url in urls:
        my_patterns += patterns('',
            url(r'^{}$'.format(my_url.url), my_url.view),
        )

    print urls


def test_load_as_template(my_patterns):

    urls_to_template = URLToTemplate.objects.all()

    for my_url in urls_to_template:
        my_template = get_template_from_string(my_url.template_content)
        my_patterns += patterns('',
            url(r'^{}$'.format(my_url.url), "wow.views.template_loader_view", {'template': my_template}),
        )

    print urls_to_template


def test_redirect_url(my_patterns):

    url_redirects = URLRedirect.objects.all()

    for r_url in url_redirects:

        my_patterns += patterns('',
            url(r'^{}$'.format(r_url.url), RedirectView.as_view(url=r_url.redirect_url)),
        )

    print url_redirects