from django import forms
from .models import Restaurant, Menu, MenuCategory
from .widgets import LocationWidget


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'category', 'address', 'account', 'tel', 'introduction', 'closedDay', 'longitude', 'latitude',
                  'businessLicenseRepresentative', 'businessLicenseMutualName', 'businessLicenseNumber', 'businessHours',
                  'area', 'representative_image', 'representative_menu', 'map_content', 'map_image']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'account': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'introduction': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'height:170px'
                }
            ),
            'closedDay': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'businessLicenseRepresentative': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'businessLicenseMutualName': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'businessLicenseNumber': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'area': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'businessHours': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
            'representative_image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'representative_menu': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '',
                }
            ),
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'category', 'price', 'image', 'content', 'soldOut']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'custom-control-input',
                    'id': 'customFile',
                    'name': 'filename',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'height: 130px'
                }
            ),
        }

    def __init__(self, admin, restaurant, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = MenuCategory.objects.filter(admin=admin, restaurant=restaurant)


class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'height: 120px',
                }
            )
        }
