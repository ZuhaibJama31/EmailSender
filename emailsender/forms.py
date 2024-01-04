from django import forms

class EmailForm(forms.Form):
   Email = forms.EmailField()
   Subject = forms.CharField(max_length= 50)
   Message = forms.CharField(max_length= 200,widget=forms.Textarea)