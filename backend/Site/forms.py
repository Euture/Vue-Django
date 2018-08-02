from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelFom):
    def clean(self):
        data = super(FeedbackForm, self).clean()
        return data

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'text')
