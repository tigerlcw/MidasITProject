from django import forms


class ExcelUploadForm(forms.Form):
    file = forms.FileField(label='excel_file')

