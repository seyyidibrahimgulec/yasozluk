from django import forms
from .models import Topic, Channel
from contents.models import Entry


class NewTopicForm(forms.ModelForm):
    # message = forms.CharField(widget=forms.Textarea(), max_length=4000,
    #                           help_text='The max length of the text is 4000.')
    # channels = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())
    channels = forms.ModelMultipleChoiceField(queryset=Channel.objects.all())

    class Meta:
        model = Topic
        labels = {
            "subject": "Başlığı girin...",
            "channels": "Etiketleri seçin..."
        }
        fields = '__all__'


class NewEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        labels = {
            "text": "İlk entry'yi siz girin..."
        }
        exclude = ('topic', 'created_by',)
