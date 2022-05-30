"""
mubo URL Configuration.

The ``urlpatterns`` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/

Examples:
    Function views
        1. Add an import: from mubo.apps.my_app import views
        2. Add a URL to urlpatterns: path("", views.home, name="home")
    Class-based views
        1. Add an import: from mubo.apps.other_app.views import Home
        2. Add a URL to urlpatterns: path("", Home.as_view(), name="home")
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns: path("blog/", include("mubo.apps.blog.urls"))

"""
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from mubo.apps.shortcodes import views as sc_views

urlpatterns = [
    path("", sc_views.index, name="index"),
    path("create-shortcode", sc_views.create_shortcode_htmx, name="create_shortcode"),
    path("<str:code>", sc_views.detail, name="detail"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
