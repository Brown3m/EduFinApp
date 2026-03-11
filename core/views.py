from django.http import JsonResponse
from core.models import Testing
from core.serializers import TestingSerializer

# Create your views here.

def testing_view(request):
	data = Testing.objects.all()
	serializer = TestingSerializer(data, many=True)
	return JsonResponse(serializer.data, safe=False)

def health_check(request):
	return JsonResponse({'status': 'ok'})

def testing_detail_view(request, id):
	try:
		data = Testing.objects.get(id=id)
	except Testing.DoesNotExist:
		return JsonResponse({'error': 'Record not found'}, status=404)

	serializer = TestingSerializer(data)
	return JsonResponse(serializer.data)