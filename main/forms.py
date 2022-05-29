from django import forms
from .models import Estate, Realtor


class EstateFilterForm(forms.Form):
    types_of_estates = [
        ('ALL', 'Все'),
        ('HOUSE', 'Дом'),
        ('FLAT', 'Квартира'),
        ('COMMERCIAL', 'Коммерческий объект'),
    ]
    types_of_deals = [
        ('ALL', 'Все'),
        ('RENT', 'Аренда'),
        ('BUY', 'Покупка'),
        ('SELL', 'Продажа'),
    ]
    type_of_object = forms.ChoiceField(choices=types_of_estates, label=False)
    type_of_deal = forms.ChoiceField(choices=types_of_deals, label=False)


class EstateForm(forms.ModelForm):
    image_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                                  label="Images")

    class Meta:
        model = Estate
        fields = "__all__"


class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = "__all__"
