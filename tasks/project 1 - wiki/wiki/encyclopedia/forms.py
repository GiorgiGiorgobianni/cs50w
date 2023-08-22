from django import forms

class NewEntryForm(forms.Form):
    title = forms.CharField(label = "Entry title", max_length=100, required=True)
    content = forms.CharField(label = "Entry content", max_length = None, widget=forms.Textarea, required=True)

class EditEntryForm(forms.Form):
    title = forms.CharField(label="Entry title", max_length = 100, widget = forms.HiddenInput, required = False)
    content = forms.CharField(label="Entry Content", max_length = None, widget = forms.Textarea, required = False)

    