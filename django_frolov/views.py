from django.shortcuts import render


def error_404(request, exception):
    message = {'error_cod': 'Error 404', 'error_message': 'Page Not Found'}
    return render(request, 'custom_error.html', message)


def error_500(request):
    message = {'error_cod': 'Error 500', 'error_message': 'Internal Server Error!'}
    return render(request, 'custom_error.html', message)
