from django import forms


class OrderForm(forms.Form):

    name = forms.CharField(
        max_length=200,
        label="Name",
        widget=forms.TextInput(attrs={
            "placeholder":"Enter your name"
        })
    )
    country = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Serbia"
            }
        )
    )
    city = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Zrenjanin"
            }
        )
    )
    postal_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"23000"
            }
        )
    )
    phone_number = forms.CharField(
        max_length=36,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone number"
            }
        )
    )