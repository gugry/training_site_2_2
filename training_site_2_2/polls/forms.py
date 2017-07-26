from django import forms


class TestForm(forms.Form):
    LABEL = ''

    CHOICES = ()

    your_name = forms.ChoiceField(label=LABEL, widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, question, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['your_name'].label = question.question_text
        CHOICE = []
        for choice in question.choice_set.all():
            CHOICE.append((choice.id, choice.choice_text,))
        self.fields['your_name'].choices = CHOICE






