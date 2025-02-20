from django.http import JsonResponse


def api_home(reuest, *args, **kwargs):
    return JsonResponse({"message": "Hi there, this is your API reson"})