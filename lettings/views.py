from django.shortcuts import render

from lettings.models import Letting


def lettings_index(request):
    """
    Displays a list of all lettings.

    Retrieves all letting objects from the database and passes them in the context
    to be rendered on the 'lettings/index.html' page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.

    Returns:
    HttpResponse
        The response with the rendered page containing the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Displays a specific letting by its ID.

    Retrieves the letting object associated with the given letting ID
    and passes its details in the context to be rendered on the 'lettings/letting.html' page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.
    letting_id: int
        The ID of the letting to be retrieved.

    Returns:
    HttpResponse
        The response with the rendered page containing the letting details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
