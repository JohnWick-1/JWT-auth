from django.shortcuts import render_to_response

def test(request):

        return render_to_response("page1.html")


def say_hello(request):

    return {'say_hello': "Hello",}