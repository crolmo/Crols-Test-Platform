import json

from django.shortcuts import render
from testhome.models import Testhome
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    testhome_list = Testhome.objects.all()
    return render(request,"index.html",{"testhome_list": testhome_list})

# Create your views here.
