from django.apps import AppConfig


class Config(AppConfig):
    name = "sentry.utils.suspect_resolutions"

    def ready(self):
        from .get_suspect_resolutions import get_suspect_resolutions  # NOQA
