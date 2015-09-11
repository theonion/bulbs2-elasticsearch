from django.conf import settings


DJES_EXCLUDED_MODELS = []

ES_CONNECTIONS = {
    "default": {
        "hosts": "localhost"
    }
}

ES_INDEX = settings.DATABASES["default"]["NAME"]

ES_INDEX_SETTINGS = {}
