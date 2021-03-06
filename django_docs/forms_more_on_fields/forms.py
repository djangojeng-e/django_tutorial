from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class CommentForm(forms.Form):
    name = forms.CharField(initial='class')
    url = forms.URLField()
    comment = forms.CharField()


class OptionalPersonForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    nick_name = forms.CharField(required=False)
