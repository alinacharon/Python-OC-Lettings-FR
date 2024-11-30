import pytest


@pytest.fixture(autouse=True)
def enable_staticfiles_storage(settings):
    settings.STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"