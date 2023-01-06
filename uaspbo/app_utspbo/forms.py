from django.forms import ModelForm
from django import forms
from app_utspbo.models import *

class formJurnal(ModelForm):
    class Meta:
        model = Jurnal
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class': 'form-control','placeholder': 'Judul', 'required' : 'required' }),
            'penulis' : forms.TextInput({'class': 'form-control','placeholder': 'Waktu Kejadian', 'required' : 'required' }),
            'penerbit' : forms.TextInput({'class': 'form-control','placeholder': 'Mag. Gempa', 'required' : 'required' }),
            'img' : forms.TextInput({'class': 'form-control','placeholder': 'Nama File Foto Jurnal', 'required' : 'required' }),
            'jumlah_halaman' : forms.NumberInput({'class': 'form-control','placeholder': 'Jumlah Halaman', 'required' : 'required' }),
            'kampus' : forms.TextInput({'class': 'form-control','placeholder': 'Koordinat', 'required' : 'required' }),
            'kelompok_ikan' : forms.TextInput({'class': 'form-control','placeholder': 'Gelombang', 'required' : 'required' }),
            'nama_latin' : forms.TextInput({'class': 'form-control','placeholder': 'Korban', 'required' : 'required' }),
        }
