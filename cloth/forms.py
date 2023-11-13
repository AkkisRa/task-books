# cloth/forms.py
from django import forms
from .models import OrderCL, TagCL


class OrderCLForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=TagCL.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    class Meta:
        model = OrderCL
        fields = ['customer', 'product', 'quantity', 'tags']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
