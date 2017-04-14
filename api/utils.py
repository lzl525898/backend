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

    # 在数据容器中删除数据
    def delValue(self, key):
        self.____dataContainer.pop(key)

    # 将数据转为http-json
    def HttpResponseDataTojson(self, data):
        return HttpResponse(json.dumps(data), content_type="application/json")

    # 返回错误信息
    def errorLog(self, data):
        self.__dataContainer.clear()
        self.__dataContainer['error'] = data
        return HttpResponse(json.dumps(self.dataContainer()), content_type="application/json")
