from django.http import HttpResponse


def home(request) -> HttpResponse:
    return HttpResponse("<h1 align=center><a href='/'>Django Project by Michail Frolov</a></h1>")
