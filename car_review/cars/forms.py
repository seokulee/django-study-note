from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(
#         label='Please write your review here',
#         widget=forms.Textarea(attrs={
#             'class':'myform',
#             'rows':15,
#             'cols':30
#         })
#     )

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # ['first_name', 'last_name', 'stars']

        labels = {
            'first_name': 'YOUR FIRST NAME',
            'last_name': 'YOUR LAST NAME',
            'stars': 'Rating'
        }

        error_messages = {
            'stars': {
                'min_value': "MIN VALUE IS 1",
                'max_value': "MAX VALUE IS 5",
            }
        }