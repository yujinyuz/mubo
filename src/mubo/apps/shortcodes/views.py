from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ShortCodeForm
from .models import ShortCode


def index(request: HttpRequest):
    return render(request, template_name="base.html")


def detail(request: HttpRequest, code: str):
    if request.method == "GET":
        shortcode = get_object_or_404(ShortCode, code=code)
        shortcode.increment_hits()

        # Browser will try to cache if `permanent=True` but we don't want that
        # because we can't increment the hits
        return redirect(to=shortcode.url, permanent=False)


def create_shortcode_htmx(request: HttpRequest):

    context = {}
    template_name = "shortcodes/fragments/create_shortcode_form.html"

    form = ShortCodeForm()

    if request.method == "POST":
        form = ShortCodeForm(data=request.POST)
        if form.is_valid():
            sc = ShortCode(
                user=None if request.user.is_anonymous else request.user,
                url=form.cleaned_data["url"],
            )
            sc.save()

            context["form"] = form
            context["code"] = sc.code

            return render(request, template_name=template_name, context=context)

    return render(request, template_name=template_name, context={"form": form})
