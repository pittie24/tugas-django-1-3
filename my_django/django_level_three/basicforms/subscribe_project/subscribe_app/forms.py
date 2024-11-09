from django import forms
from subscribe_app.models import customer

class NewSubscriber(forms.ModelForm):
    class Meta():
        model = customer
        fields = '__all__' 