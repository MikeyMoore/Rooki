from django import forms


class DocumentForm(forms.Form):
    docfile = (
        forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})),
    )
