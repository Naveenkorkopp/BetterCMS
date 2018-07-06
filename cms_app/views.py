from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import ComponentJson, ThumbnailData
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core import serializers


def index(request):
	return render(request, 'cms_app/index.html', {})


def room(request):
	return render(request, 'cms_app/room.html', {})


# To save the component object in database as well as create a static file
@csrf_exempt
def save_theme(request):
	# import ipdb;ipdb.set_trace()
	try:
		# Save the component in the database
		data = json.loads(request.body)

		component_obj = ComponentJson()
		component_obj.name = data.get('name')
		component_obj.json_data = data.get('json_data')
		component_obj.site_thumb = data.get('site_thumb')
		component_obj.save()

		# Create the window.tree object in static file
		base_dir = settings.STATIC_ROOT

		json_data = json.dumps(data)

		f = open(base_dir + '/cms_pp/cms_files/data.js', 'w+')
		f.write("window.tree = " + json_data)
		f.close()

		f1 = open(base_dir + '/cms_pp/cms_files/site_thumb.js', 'w+')
		f1.write("window.site_thumb = " + data.get('site_thumb'))
		f1.close()

	except Exception as e:
		return JsonResponse({'status': False})
	finally:
		if f is not None:
			f.close()
		if f1 is not None:
			f1.close()


	return JsonResponse({'status': True})


# To save the thumbnail object getting from the front end
@csrf_exempt
def save_thumbnail(request):
	# import ipdb;ipdb.set_trace()
	try:

		data = json.loads(request.body)

		thumbnail_obj = ThumbnailData()
		thumbnail_obj.thumbnail_name = data.get('name')
		thumbnail_obj.thumbnail_title = data.get('title')
		thumbnail_obj.thumbnail_content = data.get('content')
		thumbnail_obj.save()

	except Exception as e:
		return JsonResponse({'status': False})

	return JsonResponse({'status': True})


# To get the component based on slug name from database
def get_theme(request, slug):
	# import ipdb;ipdb.set_trace()

	try:
		component_obj = ComponentJson.objects.get(name=slug)
		serialized_data = serializers.serialize('json', [component_obj,])
		struct = json.loads(serialized_data)
		# data = json.dumps(struct[0])
	except Exception as e:
		return JsonResponse({'status': False})

	return JsonResponse(struct,safe=False)


