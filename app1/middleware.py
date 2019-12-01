from django.http import HttpResponse
from rest_framework.response import Response
import json
from django.contrib.redirects.middleware import RedirectFallbackMiddleware


class MyMiddleware1:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before processing')
        response=self.get_response(request)
        print('after processing')
        return response

    def process_request(self, request):
        # request.foo = 'bar'
        print('*'*50)
        request.POST['name']='danny'

    def process_view(self,request, view_func, *view_args, **view_kwargs):
        print(request)
        print(view_func)

        # print(request.POST['name'])
        return

    def process_exception(self,request,exception):
        print('inside exception')
        msg='<h1>ERROR OCCURE IN FUNCTION</h1>'
        msg2='{}'.format(exception.__class__.__name__)
        msg3='{}'.format(exception)
        msg4='{}'.format(request)
        return HttpResponse(msg+'<br><h3>'+msg2+'<br>'+msg3+'<br>'+msg4+'</h3>')

    def process_template_response(self, request, response):
        print('inside process_template_response')
        print(request.POST)
        print(response.context_data) # dict
        response.context_data['title'] = 'We changed the title'
        # response.template_name='page2.html'
        return response




class MyMiddleware2:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before procesing2')
        response=self.get_response(request)
        print('after processing2')
        return response



def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
