from django.apps import AppConfig


class TeammatchesConfig(AppConfig):
    name = 'TeamMatches'

    def ready(self):
        import TeamMatches.signals
