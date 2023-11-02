from django import forms
from .models import MyCarModel

class MyCarForm(forms.ModelForm):
  class Meta:
    model = MyCarModel
    fields = [
      "make",
      "model",
      "year",
      "nickname"
    ]





