from django import forms
from .models import Employe


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ["first_name", "last_name", "email", "position", "salary"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full mt-2",
                    "placeholder": "Prénom",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full mt-2",
                    "placeholder": "Nom",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input input-bordered w-full mt-2",
                    "placeholder": "Email",
                }
            ),
            "position": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full mt-2",
                    "placeholder": "Poste",
                }
            ),
            "salary": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full mt-2",
                    "placeholder": "Salaire",
                }
            ),
        }
