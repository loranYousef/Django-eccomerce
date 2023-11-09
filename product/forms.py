from django import forms
from .models import Reviews


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment', 'rate']