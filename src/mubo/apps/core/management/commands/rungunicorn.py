import os
import sys
from django.core.management.base import BaseCommand
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command


class Command(BaseCommand):
    help = "Runs the Django application using the Gunicorn server"

    def add_arguments(self, parser):
        parser.add_argument(
            "--host", type=str, default="0.0.0.0", help="Host to run the server on"
        )
        parser.add_argument(
            "--port", type=int, default=8000, help="Port to run the server on"
        )
        parser.add_argument(
            "--workers", type=int, default=3, help="Number of worker processes"
        )
        parser.add_argument("--reload", action="store_true", help="Enable auto-reload")

    def handle(self, *args, **options):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mubo.conf.settings")

        self.stdout.write("Collecting static files...")
        call_command("collectstatic", interactive=False, verbosity=0)

        from gunicorn.app.wsgiapp import WSGIApplication

        class DjangoApplication(WSGIApplication):
            def load_wsgiapp(self):
                return get_wsgi_application()

        gunicorn_args = [
            "gunicorn",
            f"--bind={options['host']}:{options['port']}",
            f"--workers={options['workers']}",
            "--access-logfile=-",  # temporarily put this here since we don't have nginx
            "mubo.wsgi:application",
        ]

        if options["reload"]:
            gunicorn_args.append("--reload")

        self.stdout.write(
            self.style.SUCCESS(
                f"Starting Gunicorn server on {options['host']}:{options['port']} with {options['workers']} workers"
            )
        )

        sys.argv = gunicorn_args
        DjangoApplication().run()
