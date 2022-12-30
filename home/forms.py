from django import forms
from django.contrib.auth.models import User
from home.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.
class UserForm(UserCreationForm):
	email = form.EmailField()
	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		labels = {
			'password1':'Password',
			'password2':'Confirm Password'
		}
class UserProfileInfoForm(forms.ModelForm):
	bio = forms.CharField(required=False)
	teacher = 'teacher'
	student = 'student'
	parent = 'parent'
	user_types = [
		(parent, 'parent'),
		(student, 'student'),
	]
	user_type = forms.ChoiceField(required=True, choices=user_types)
	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_pic', 'user_type')
