# Mubo

Describe your project in one sentence.

## Demo

https://github.com/yujinyuz/mubo/assets/10972027/c30c76af-cb16-433c-9dc0-c33c0b0c1808

## Quickstart

Install the project and the development dependencies into a [virtual environment](https://docs.python.org/3.7/tutorial/venv.html):

```console
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip wheel hatch
python3 -m pip install --editable ".[dev]"

export DJANGO_DEBUG=true
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

## Starting a New App

To create an app

```console
make app name=<app_name>
```

## Deployment

The following list describes only the absolute necessary steps to outline a deployment for a Django project wheel. For example a component to serve static files is missing - you could use [WhiteNoise](https://github.com/evansd/whitenoise/) to do this.

Also see [How to use Django with Gunicorn](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/) and [Deployment Checklist](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/) for more information.


1. Add your favorite WSGI HTTP server, e.g.  [Gunicorn](https://gunicorn.org/), to `dependencies` in `pyproject.toml`.
2.  [Build](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives) a [wheel](https://github.com/pypa/wheel) of the project.
    ```console
    hatch build
    ```
3. Generate the .pex file
    ```console
    pex dist/*.whl -o mubo.pex -c mubo
    ```
4. Copy the `.pex` from the `dist` directory to the server to be deployed.
5. Create a minimal configuration on the server using environment variables.
    ```bash
    export DJANGO_SETTINGS_MODULE=mubo.conf.settings
    export DJANGO_ALLOWED_HOSTS=www.example.com
    export DJANGO_DEBUG=False
    ```
6. If this is the first time being deployed, make sure to run `./mubo.pex migrate` command.
7. Start the gunicorn webserver like this:
   ```console
   ./mubo.pex rungunicorn  # automatically calls `collectstatic`
   ```

