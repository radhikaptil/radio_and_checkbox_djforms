from secrets import choice
from django import forms

g=[('male','male'),('female','female')]

c=[('Python','Python'),('Django','Django'),('API','API')]

class RegistrationForm(forms.Form):
    Name=forms.CharField(max_length=10)
    Age=forms.IntegerField()
    Password=forms.CharField(max_length=10,widget=forms.PasswordInput)

    #choose one element using dropdown list
    #Gender=forms.ChoiceField(choices=g)

    #choose one input element by using radioselect
    Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)

    #choose multiple input elements by using dropdown list
    #Courses=forms.MultipleChoiceField(choices=c)

    #choose multiple input element by using checkbox
    Courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)








