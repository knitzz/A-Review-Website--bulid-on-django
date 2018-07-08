from django.contrib.auth import get_user_model
from django import forms
from django.forms import TextInput

User=get_user_model()

class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	password1.widget.attrs.update({'class':'input pass'})
	password2.widget.attrs.update({'class':'input pass'})
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email',)
		widgets = {
            'username': TextInput(attrs={'class':'input pass'}),
            'first_name' : TextInput(attrs={'class':'input pass'}),
            'last_name' : TextInput(attrs={'class':'input pass'}),
            'email': TextInput(attrs={'class':'input pass'}),
        }

	def clean_email(self):
		email=self.cleaned_data.get('email')
		qs=User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("email already registered")
		return email

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		# user.is_active = False
		# # create a new user hash for activating email.

		if commit:
			user.save()
			# user.profile.send_activation_email()
		return user
