from django import forms
from .models import Diary
from .models import Todo
from .models import Image
 
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'title', 'text','tagname')
        widgets = {#辞書型のデータ
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.DateInput(attrs={'class': 'form-control'}),
            'text': forms.DateInput(attrs={'class': 'form-control'}),
            'tagname': forms.DateInput(attrs={'class': 'form-control'}),
        }
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('time','memo')
        widgets = {
            'time': forms.DateInput(attrs={'class':'form-control'}),
            'memo': forms.DateInput(attrs={'class':'form-control'}),
        }        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','name','memo','today')