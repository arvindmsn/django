from django import forms
from sample.models import Question

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		exclude = ('publication_date',)
