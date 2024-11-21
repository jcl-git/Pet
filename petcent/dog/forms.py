from django.forms import ModelForm,Textarea
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model=Review
        fields=['text','watchAgain']
        labels={
            'text':('说说你是否喜欢它吧'),
            'watchAgain':('是否想购买'),
        }
        widgets={
            'text':Textarea(attrs={'rows':4}),
        }