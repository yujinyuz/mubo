# Use an official Python runtime as a parent image
FROM python:3.11-slim AS deps

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN pip install wheel hatch pex

RUN hatch build

RUN pex dist/*.whl -o mubo.pex -c mubo


FROM python:3.11-slim
WORKDIR /usr/src/app

COPY --from=deps /usr/src/app/mubo.pex /usr/src/app/mubo.pex

RUN chmod +x mubo.pex

ENV DJANGO_SETTINGS_MODULE mubo.conf.demo_settings
ENV DJANGO_ALLOWED_HOSTS "localhost,127.0.0.1,0.0.0.0"

RUN ./mubo.pex migrate

ENTRYPOINT ["./mubo.pex", "rungunicorn"]
