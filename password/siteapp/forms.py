from django.forms import ModelForm

from siteapp.models import Site


class SiteForm(ModelForm):
    class Meta:
        model = Site

    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        self.fields.pop('work')
        self.fields.pop('notwork')
