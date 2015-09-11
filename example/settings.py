CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


DEBUG = True


INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "djes",
    "bulbs2_elasticsearch",
    "example.app",
)


SECRET_KEY = "you'll never guess what my secret key is"


TIME_ZONE = "America/Chicago"


USE_TZ = True


ES_INDEX = "bulbs2-elasticsearch-example"


ES_INDEX_SETTINGS = {
    "bulbs2-elasticsearch-example": {
        "index": {
            "number_of_replicas": 1,
            "analysis": {
                "filter": {
                    "autocomplete_filter": {
                        "type": "edge_ngram",
                        "min_gram": 1,
                        "max_gram": 20
                    }
                },
                "analyzer": {
                    "autocomplete": {
                        "type":      "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "lowercase",
                            "autocomplete_filter"
                        ]
                    }
                }
            }
        },
    }
}


ES_CONNECTIONS = {
    "default": {
        "hosts": "localhost"
    }
}
