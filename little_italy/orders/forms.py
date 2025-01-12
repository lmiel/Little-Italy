from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    address = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    card_number = forms.CharField(
        max_length=16, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    expiry_date = forms.CharField(
        max_length=5, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    cvv = forms.CharField(
        max_length=3, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    total_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
