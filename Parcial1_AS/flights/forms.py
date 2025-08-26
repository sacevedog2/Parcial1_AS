from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model  = Flight
        fields = ['name', 'ftype', 'price']
        widgets = {
            'ftype': forms.Select(choices=Flight.FlightType.choices)
        }

    def clean_price(self):
        p = self.cleaned_data['price']
        if p <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return p
