from django import forms

class NameForm(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    your_name = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


# class NameForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
#     CHOICES = (('1', 'First',), ('2', 'Second',))


