from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from .models import mahasiswa, dosen, jurusan, User
from bootstrap_modal_forms.forms import BSModalModelForm

# iterable



# creating a form
USER_CHOICES = (
    (1, 'Mahasiswa'),
    (2, 'Dosen')
    
)

class MHSdetailForm(forms.ModelForm):

    class Meta:
        model = mahasiswa
        fields = ['nama', 'id_jurusan']


class skripsidetailForm(forms.ModelForm):

    class Meta:
        model = mahasiswa
        fields = ['judul', 'pembimbing1', 'pembimbing2','abstrak','abstract', 'bab1','bab2','bab3','bab4','bab5','daftar_pustaka']

class MHSModelForm(BSModalModelForm):
    
    class Meta:
        model = mahasiswa
        fields = ['nama', 'id_jurusan','judul', 'pembimbing1', 'pembimbing2', 'abstrak','abstract', 'bab1', 'bab2', 'bab3', 'bab4', 'bab5', 'daftar_pustaka']


class DosenModelForm(BSModalModelForm):

    class Meta:
        model = dosen
        fields=['nama', 'id_jurusan']
        
        
class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_CHOICES)
    class Meta:
        model = User
        fields = ['username', 'user_type', 'password1', 'password2']

