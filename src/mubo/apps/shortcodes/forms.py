from django import forms

from .models import ShortCode


class ShortCodeForm(forms.ModelForm):
    class Meta:
        model = ShortCode
        fields = [
            "url",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["url"].help_text = ""
