from django.http import JsonResponse

from app.errors import ObjectAlreadyExists, ValidationError, ObjectDoesNotExist


class KeyErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if exception.__class__ is KeyError:
            return JsonResponse({"Error": str(exception)}, status=400)


class ObjectAlreadyExistsHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if exception.__class__ is ObjectAlreadyExists:
            return JsonResponse({"Error": str(exception)}, status=400)


class ValidationErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if exception.__class__ is ValidationError:
            return JsonResponse({"Error": str(exception)}, status=400)


class ObjectDoesNotExistHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if exception.__class__ is ObjectDoesNotExist:
            return JsonResponse({"Error": str(exception)}, status=400)
