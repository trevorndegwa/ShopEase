from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm

class SignUpForm(UserCreationForm):
        # Define an email field with a custom widget and placeholder
        email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
        # Define a first name field with a custom widget and placeholder
        first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
        # Define a last name field with a custom widget and placeholder
        last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

        class Meta:
                # Specifies the User model to be used for the form and links it 
                model = User
                fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# Initialise the form and customise widgets, placeholders, and help text
        def __init__(self, *args, **kwargs):
                # Call the parent class's constructor to ensure proper initialisation
                super(SignUpForm, self).__init__(*args, **kwargs)
                
                # Customise the username field
                self.fields['username'].widget.attrs['class'] = 'form-control'
                self.fields['username'].widget.attrs['placeholder'] = 'User Name'
                self.fields['username'].label = ''
                self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

                # Customise the password1 field (primary password)
                self.fields['password1'].widget.attrs['class'] = 'form-control'
                self.fields['password1'].widget.attrs['placeholder'] = 'Password'
                self.fields['password1'].label = ''
                self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

                # Customise the password2 field (password confirmation)
                self.fields['password2'].widget.attrs['class'] = 'form-control'
                self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
                self.fields['password2'].label = ''
                self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class UserUpdateForm(UserChangeForm):
        # Hide password stuff
        password = None
        # Define an email field with a custom widget and placeholder
        email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=False)
        # Define a first name field with a custom widget and placeholder
        first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), required=False)
        # Define a last name field with a custom widget and placeholder
        last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), required=False)

        class Meta:
                # Specifies the User model to be used for the form and links it 
                model = User
                fields = ('username', 'first_name', 'last_name', 'email')

# Initialise the form and customise widgets, placeholders, and help text
        def __init__(self, *args, **kwargs):
                # Call the parent class's constructor to ensure proper initialisation
                super(UserUpdateForm, self).__init__(*args, **kwargs)
                
                # Customise the username field
                self.fields['username'].widget.attrs['class'] = 'form-control'
                self.fields['username'].widget.attrs['placeholder'] = 'User Name'
                self.fields['username'].label = ''
                self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class PasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
    
    # Initialise the form and customise widgets, placeholders, and help text
    def __init__(self, *args, **kwargs):
        # Call the parent class's constructor to ensure proper initialisation
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        # Customise the password1 field (primary password)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # Customise the password2 field (password confirmation)
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
    address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=False)
    address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
    county = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'County'}), required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
    postalcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Postal Code'}), required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'county', 'city', 'postalcode', 'country')
