from django.test import TestCase

from django import forms
from django.contrib.postgres.forms import HStoreField


class HStoreForm(forms.Form):
    f1 = HStoreField()


class TextForm(forms.Form):
    f1 = forms.Textarea()


form_w_hstore = HStoreForm()
assert form_w_hstore.has_changed() is False #Fails

form_w_textarea = TextForm()
assert form_w_textarea.has_changed() is False #Passes
