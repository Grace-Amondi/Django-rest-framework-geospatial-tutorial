# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import HStoreField

class School(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100, null=True)
    enrollment = models.IntegerField()
    location = models.PointField(srid=4326)
    electricity_availability = models.BooleanField(default=False)
    emmis_code = models.IntegerField(null=False,default=0)

    def __unicode__(self):
        return self.name

class Link(models.Model):
    """
    Metadata is stored in a PostgreSQL HStore field, which allows us to
    store arbitrary key-value pairs with a link record.
    """
    metadata = HStoreField(blank=True, null=True, default=dict)
    geo = models.LineStringField()
    objects = models.GeoManager()
