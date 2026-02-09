from django import forms
from cbvapp.models import company, product


class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = "__all__"


class EMIForm(forms.Form):
    prod_name = forms.CharField(disabled=True, required=False, label="Product")
    price = forms.IntegerField(disabled=True, required=False, label="Car Price")
    loan_amount = forms.IntegerField(min_value=0, label="Loan Amount")

    TENURE_CHOICES = [
        (1, "1 year"),
        (2, "2 years"),
        (3, "3 years"),
        (5, "5 years"),
        (7, "7 years"),
    ]

    tenures = forms.ChoiceField(
        choices=TENURE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Tenure (years)",
    )

    annual_rate = forms.DecimalField(
        initial=12.0, min_value=0, label="Annual Interest Rate (%)"
    )

    def clean(self):
        cleaned = super().clean()
        loan = cleaned.get("loan_amount")

        # price is provided via form initial data
        price = self.initial.get("price") if hasattr(self, "initial") else None
        if price is None:
            # try to get from cleaned data (if someone tampered)
            price = cleaned.get("price")

        if loan is not None and price is not None:
            try:
                if int(loan) > int(price):
                    raise forms.ValidationError(
                        "Loan amount must be less than or equal to the car price."
                    )
            except ValueError:
                pass

        return cleaned