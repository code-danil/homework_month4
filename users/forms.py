from django import forms
from .models import ITSpecialist
from captcha.fields import CaptchaField


class ITSpecialisForm(forms.ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки')

    class Meta:
        model = ITSpecialist
        fields = '__all__'