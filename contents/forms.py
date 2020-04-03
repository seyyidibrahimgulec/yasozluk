from django import forms
from .models import Topic, Channel


class NewTopicForm(forms.ModelForm):
    # message = forms.CharField(widget=forms.Textarea(), max_length=4000,
    #                           help_text='The max length of the text is 4000.')
    # channels = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())
    channels = forms.ModelMultipleChoiceField(queryset=Channel.objects.all())

    class Meta:
        model = Topic
        fields = '__all__'
