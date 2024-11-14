from django import forms
from web.models import Plataforma

class PlataformaForm(forms.Form):
    plataforma = forms.ModelChoiceField(
        queryset=Plataforma.objects.all(),
        required=False,
        empty_label="Todas las plataformas",
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'this.form.submit();'})

 )
    