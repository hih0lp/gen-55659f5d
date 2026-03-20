from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client_name', 'client_phone', 'delivery_address', 'product', 'comment']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'client_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 999-99-99'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Адрес доставки'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Дополнительные пожелания'}),
        }