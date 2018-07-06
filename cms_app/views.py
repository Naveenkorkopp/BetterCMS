from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import ComponentJson, 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from django.core import serializers

def index(request):
    return render(request, 'cms_app/index.html', {})

def room(request, room_name):
    return render(request, 'cms_app/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def check(request):
	return render(request, 'cms_app/check.html', {})

@csrf_exempt
def save_theme(request):
	import ipdb;ipdb.set_trace();

	component_obj = ComponentJson()

	component_obj.name = str(request.POST['name'])
	component_obj.json_data = json.dumps(request.POST['json_data'])

	component_obj.save()

	return JsonResponse({'status':True})

def get_theme(request):
	comp_obj =ComponentJson.objects.all()

	serializer_data = serializers.serializer('json',comp_obj)

	return JsonResponse(serializer_data)

