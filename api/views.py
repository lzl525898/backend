# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .utils import DataStore

def index():
    return None

def demo(request):
    dataStore = DataStore(request)

    dataStore.appendValue('name', dataStore.requestValue('name'))

    dataStore.appendValue('key1', 'value1')

    return dataStore.HttpResponseDataTojson(dataStore.dataContainer())
