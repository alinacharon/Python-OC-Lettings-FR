from django.shortcuts import render


def index(request):
    """
    Displays the main page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.

    Returns:
    HttpResponse
        The response with the rendered main page.
    """
    return render(request, 'index.html')


def error_404(request, exception):
    """
    Displays a custom 404 error page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.
    exception: Exception
        The exception that triggered the 404 error.

    Returns:
    HttpResponse
        The response with the rendered 404 error page.
    """
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Displays a custom 500 error page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.

    Returns:
    HttpResponse
        The response with the rendered 500 error page.
    """
    return render(request, '500.html', status=500)
