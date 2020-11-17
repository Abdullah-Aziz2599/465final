from django import forms
from feed.models import FeedItem


class TaskForm(forms.ModelForm):
    class Meta:
        model = FeedItem
        fields = [
            'comment',
        ]
        widgets = { 'comment': forms.TextInput(attrs={'size': 80})}
