import os

os.environ["DJANGO_SETTINGS_MODULE"] = "travelds.settings"

import django
from travelds import settings as overridden_settings
from django.conf import settings


default_app_config = "travelds.apps.TravelDSConfig"

if not settings.configured:
    # Get the list of attributes the module has
    attributes = dir(overridden_settings)
    conf = {}

    for attribute in attributes:
        # If the attribute is upper-cased i.e. a settings variable, then copy it into conf
        if attribute.isupper():
            conf[attribute] = getattr(overridden_settings, attribute)

    # Configure settings using the settings
    settings.configure(**conf)

    # This is needed since it is a standalone django package
    django.setup()

from travelds.console import console_entry_point
