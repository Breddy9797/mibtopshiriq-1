from django import forms
from .models import Topshiriq


class TopshiriqForm(forms.ModelForm):
    class Meta:
        model = Topshiriq
        fields = ['topshiriq_raqami', 'topshiriq_turi', 'qisqacha_mazmun', 'toliq_mazmun', 'holat', 'ijrochi', 'kanal',
                  'kim_tomonidan', 'prioritet', 'ilova', 'izoh', 'muddat']

        widgets = {
            'topshiriq_raqami': forms.TextInput(attrs={'class': 'span6'}),
            'topshiriq_turi': forms.Select(attrs={'class': 'span6 m-wrap'}),
            'qisqacha_mazmun': forms.TextInput(attrs={'class': 'span6'}),
            'toliq_mazmun': forms.Textarea(attrs={'class': 'span6 m-wrap', 'id': 'typeahead'}),
            'holat': forms.Select(attrs={'class': 'span6 m-wrap'}),
            'ijrochi': forms.Select(attrs={'class': 'span6 m-wrap'}),
            'kanal': forms.Select(attrs={'class': 'span6 m-wrap'}),
            'kim_tomonidan': forms.Select(attrs={'class': 'span6 m-wrap'}),
            'prioritet': forms.Select(attrs={'class': 'span6 m-wrap'}),
            'ilova': forms.FileInput(attrs={'class': 'input-file uniform_on'}),
            'izoh': forms.Textarea(attrs={'class': 'span6 m-wrap'}),
            'muddat': forms.SelectDateWidget(),
        }
