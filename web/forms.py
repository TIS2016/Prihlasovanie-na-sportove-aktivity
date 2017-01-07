from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import authenticate, login, get_user_model, logout


class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class UserRegisterForm(forms.ModelForm):
    CHOICES = [('student', 'student'),
               ('ucitel', 'ucitel')]

    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    employee = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'employee', 'password']



        # def clean(self,*args,**kvargs):
        #     username = self.cleaned_data.get("username")
        #     password = self.cleaned_data.get("password")
        #
        #     user = authenticate(username=username, password=password)
        #     if not user:
        #         raise forms.ValidationError("This user does not exist")
        #     if not user.check_password(password):
        #         raise forms.ValidationError("Incorrect password")
        #     if not user.is_active:
        #         raise forms.ValidationError("This user is no longer active")
        #     return super(UserLoginForm, self).clean(*args, **kvargs)