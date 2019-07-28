from __future__ import absolute_import
from django import forms
from .models import Portfolio


class PortfolioPost(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title','image','description']
