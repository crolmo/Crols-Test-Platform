from django.shortcuts import render
from django.http import HttpResponse
from server import models
import json
import uuid
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response

def write_server(request):
    data = json.loads(request.body)
    data['id'] = uuid.uuid4()
    models.Person.objects.create(**data)
    res = {
        'success': True
    }

    return HttpResponse(json.dumps(res),content_type='application/json')


def read_server(request):
    data = serializers.serialize('python', models.Person.objects.all())
    res = {
        'success': True,
        'data': data
    }
    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='Application/json')

class Test(APIView):
    def get(self,request):
        a = request.GET['a']
        res = {
            'success': True,
            'data': 'a'
        }
        return Response()