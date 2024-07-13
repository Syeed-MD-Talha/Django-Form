from django import forms
from .models import reviewModel

# class reviewForm(forms.Form):
#     username=forms.CharField(label="Your name", max_length=100,error_messages={
#         'required':"Your name must not be empty!",
#         'max_length':'Please enter a shortest name!',
#     })
#     review_text=forms.CharField(label="Your feedback",widget=forms.Textarea)
#     rating=forms.IntegerField(label='Your rating',min_value=1,max_value=5)


#---------------------- shortcut -----------
class reviewForm(forms.ModelForm):
    class Meta:
        model=reviewModel
        fields='__all__'
        # fields=['username','review','rating']
        labels={
            'username':'Enter your name',
            'review':'Your feedback',
            'rating':'Please add rating'
        }
        error_messages={
            'username':{
                'required':'Your name must not be empty!',
                'max_lenght':'Please enter a shorter name!'
            }
        }