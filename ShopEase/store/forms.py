from django import forms
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
        email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
        # Define a first name field with a custom widget and placeholder
        first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
        # Define a last name field with a custom widget and placeholder
        last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

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
