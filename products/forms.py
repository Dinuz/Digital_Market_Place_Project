from django import forms
from django.utils.text import slugify

from .models import Product

PUBLISH_CHOICES = (
    #('', ''),
    ('draft', 'Draft'),
    ('publish', 'Publish'),
)


class ProductAddForm(forms.Form):
    title = forms.CharField(label='Your Title', widget=forms.TextInput(
        attrs={
            'class': 'my-custom-class',
            'placeholder': 'Title',
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'my-actual-class',
            'placeholder': 'description',
            'some-attr': 'this',
        }
    ))
    price = forms.DecimalField()
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 1.00:
            raise forms.ValidationError('Price must be greater than 1')
        elif price >= 99.99:
            raise forms.ValidationError('Price must be smaller than 100')
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <= 3:
            raise forms.ValidationError('Title must be greater than 3')
        else:
            return title


class ProductModelForm(forms.ModelForm):
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)
    #title = forms.CharField(label='Your Title', widget=forms.TextInput(
    #    attrs={
    #        'class': 'my-custom-class',
    #        'placeholder': 'Title',
    #    }
    #))
    #description = forms.CharField(widget=forms.Textarea(
    #    attrs={
    #        'class': 'my-actual-class',
    #        'placeholder': 'description',
    #        'some-attr': 'this',
    #    }
    #))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'my-actual- class ',
                    'placeholder': 'description',
                    'some-attr': 'this',
                }
            )
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
        #title = cleaned_data.get('title')
        #slug = slugify(title)
        #s = Product.objects.filter(slug=slug).exists()
        #if qs:
        #    raise forms.ValidationError('Title is taken. Please try again.')
        #print(cleaned_data)
        return cleaned_data


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 1.00:
            raise forms.ValidationError('Price must be greater than 1')
        elif price >= 99.99:
            raise forms.ValidationError('Price must be smaller than 100')
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <= 3:
            raise forms.ValidationError('Title must be greater than 3')
        else:
            return title









