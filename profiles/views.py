import sentry_sdk
from django.http import Http404
from django.shortcuts import render

from profiles.models import Profile


def profiles_index(request):
    """
    Displays a list of all profiles.

    Retrieves all profile objects from the database and passes them in the context
    to be rendered on the 'profiles/index.html' page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.

    Returns:
    HttpResponse
        The response with the rendered page containing the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Displays a specific profile by username.

    Retrieves the profile object associated with the given username
    and passes it in the context to be rendered on the 'profiles/profile.html' page.

    Parameters:
    request: HttpRequest
        The request object containing information about the current request.
    username: str
        The username for which the profile will be retrieved.

    Returns:
    HttpResponse
        The response with the rendered page containing the profile information.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        sentry_sdk.capture_exception(
            f"Profile matching query does not exist for username: {username}")

        raise Http404("Profile not found")

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
