from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1 align=center>Welcome to "Hillel Homework Django Project"</h1>'
                        '<p align=center>by Michail Frolov</p>')
