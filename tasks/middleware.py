from django.http import HttpResponse

class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        print("middleware")
        response = self._get_response(request)
        return response

    def process_exception(self, request, exception):
        print("Exception")
        return HttpResponse("Exception")