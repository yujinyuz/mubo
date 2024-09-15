from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        from django.conf import settings

        self.stdout.write(f"{settings.BASE_DIR=}")
        self.stdout.write(f"{settings.PROJECT_DIR=}")
