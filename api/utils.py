#coding=utf-8
from django.http import HttpResponse

import json

class DataStore:
    # 数据容器
    __dataContainer = {}

    # 初始化
    def __init__(self, request):
        self.request = request

    # 从请求中中获取数据
    def requestValue(self, key):
        if self.request.method == 'GET':
            return self.request.GET.get(key, None)
        else:
            return self.request.POST.get(key, None)

    # 获取数据容器
    def dataContainer(self):
        return self.__dataContainer

    # 向数据容器中添加数据
    def appendValue(self, key, value):
        self.__dataContainer[key] = value

    # 将数据转为http-json
    def HttpResponseDataTojson(self, data):
        return HttpResponse(json.dumps(data), content_type="application/json")
