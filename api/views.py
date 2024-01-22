from django.http import HttpResponse, JsonResponse


def index(request):
    return JsonResponse({"message": "Hello, world!"})