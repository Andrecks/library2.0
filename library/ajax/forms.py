from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name",
                 "father_name", "email", "password1", "password2",
                 "phone")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user