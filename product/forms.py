from django import forms

from product.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {"text": ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 89, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].initial = ""
