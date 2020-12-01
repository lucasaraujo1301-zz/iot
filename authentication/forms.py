from django import forms
from comum.models import *
from localflavor.br.forms import BRCPFField
from django.utils.translation import ugettext_lazy as _


class NewUserForm(forms.ModelForm):
    birth_date = forms.DateField(label=u'Birth Date',
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
                                 input_formats=('%d/%m/%Y',))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label=_("Password"), min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Password confirmation"), min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = Usuario
        fields = ('name', 'cpf', 'birth_date')
        labels = {'cpf': 'CPF'}

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")

        if cpf:
            validation_cpf = BRCPFField()
            validation_cpf.clean(cpf)

        return cpf

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(u'The passwords dont match')
        return self.cleaned_data
