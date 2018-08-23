from django import forms
from .models import skillsMatrix

class PersonForm(forms.ModelForm):
    class Meta:
        model = skillsMatrix
        fields = ['skillsMatrixEmployee', 'skillsMatrixSkills', 'proficiency', 'levelOfInterest']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skillsMatrixSkills'].queryset = skillsMatrix.objects.none()