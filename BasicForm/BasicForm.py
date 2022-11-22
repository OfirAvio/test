from django import forms


class ContactForm(forms.Form):
    UserID = forms.IntegerField(label='User ID')
    Serial = forms.CharField(label='Serial Number')
    ProblemDescription = forms.CharField(label='Problem Description', widget=forms.Textarea)
    Indicator1 = forms.ChoiceField(label='Indicator1', choices=[('on', 'On'), ('off', 'Off'), ('blinking', 'Blinking')])
    Indicator2 = forms.ChoiceField(label='Indicator2', choices=[('on', 'On'), ('off', 'Off'), ('blinking', 'Blinking')])
    Indicator3 = forms.ChoiceField(label='Indicator3', choices=[('on', 'On'), ('off', 'Off'), ('blinking', 'Blinking')])
