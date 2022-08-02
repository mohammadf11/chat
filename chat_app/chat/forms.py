from django import forms

class MessageBarForm(forms.Form):
    message_bar = forms.CharField(label='')
    message_bar.widget.attrs.update({ 'type':"text" , 'placeholder':"Write your message..."})
