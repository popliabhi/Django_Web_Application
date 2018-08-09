from django import forms
from .models import my_blog


class HomeForm(forms.ModelForm):
	class Meta:
		model=my_blog 
		fields=('author','title','description',)
