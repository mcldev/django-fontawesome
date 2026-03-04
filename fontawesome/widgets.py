from django import forms
from django.conf import settings
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from .utils import get_icon_choices

CHOICES = get_icon_choices()

class IconWidget(forms.Select):

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=CHOICES)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        option["attrs"]["data-icon"] = value
        return option

    class Media:

        js = (
            'fontawesome/select2/select2.min.js',
            'fontawesome/js/django_fontawesome.js',
        )

        css = {
            'all': (
                getattr(settings, 'FONTAWESOME_CSS_URL', 'fontawesome/css/font-awesome.min.css'),
                'fontawesome/select2/select2.css',
                'fontawesome/select2/select2-bootstrap.css'
            )
        }
