from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Наименование')
    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.Textarea
    )
    price = forms.DecimalField(
        label='Стоимость',
        max_digits=7,
        decimal_places=2
    )
    image = forms.URLField(label='Изображение')
    category = forms.IntegerField(label='Категория')
    stock = forms.IntegerField(label='Остаток', min_value = 0)