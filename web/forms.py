from .models import SchoolUser
from django import forms
from django.utils.safestring import mark_safe


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SchoolUser
        fields = ['username', 'password']


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # function = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
    #                              required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    # function = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
    #                                   widget=forms.RadioSelect(choices=[(1, 'Student'), (0, 'Ucitel')],
    #                                                            renderer=HorizontalRadioRenderer))
    function = forms.BooleanField(required=False, initial=True,
                                  widget=forms.RadioSelect(choices=[(True, 'Student'), (False, 'Ucitel')],
                                                           renderer=HorizontalRadioRenderer))

    class Meta:
        model = SchoolUser
        fields = ['username', 'first_name', 'last_name', 'email', 'function', 'password']
