__author__ = 'Happy'

from django.http import HttpResponse


def hello(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello world")
