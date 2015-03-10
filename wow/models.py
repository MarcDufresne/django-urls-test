# -*- coding: utf-8 -*-
"""

"""
from django.db import models


class URLTest(models.Model):

    url = models.URLField()
    view = models.CharField(max_length=255)


class URLToTemplate(models.Model):

    url = models.URLField()
    template_content = models.TextField()


class URLRedirect(models.Model):

    url = models.URLField()
    redirect_url = models.URLField()