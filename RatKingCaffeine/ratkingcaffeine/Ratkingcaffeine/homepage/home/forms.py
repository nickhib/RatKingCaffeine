from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models




class userinformation(forms.Form):
        first_name_field = forms.CharField(label= "First Name", max_length=280)
        last_name_field = forms.CharField(label= "Last Name",max_length=280)
        phone_number = forms.CharField(label = "Phone number",max_length=280)
        address_field = forms.CharField(label = 'address',max_length=280)
        city_field = forms.CharField(label = 'City',max_length=280)
        zipcode_field = forms.IntegerField(label ='zipcode')
        def save(self, request):
                existing = models.userinformation.objects.filter(u=request.user)
                if existing:
                        existing.update(First_name=self.cleaned_data["first_name_field"],Last_name = self.cleaned_data["last_name_field"],phone_number = self.cleaned_data["phone_number"],address = self.cleaned_data["address_field"],city = self.cleaned_data["city_field"], zipcode = self.cleaned_data["zipcode_field"])
                        return existing
                else:
                        info_instance = models.userinformation()
                        info_instance.First_name = self.cleaned_data["first_name_field"]
                        info_instance.Last_name = self.cleaned_data["last_name_field"]
                        info_instance.phone_number = self.cleaned_data["phone_number"]
                        info_instance.address = self.cleaned_data["address_field"]
                        info_instance.city = self.cleaned_data["city_field"]
                        info_instance.zipcode = self.cleaned_data["zipcode_field"]
                        info_instance.u = request.user
                        info_instance.save()
                        return info_instance

class usercommentsForm(forms.Form):
	comment_field = forms.CharField(label="please type comment here:",max_length=280)

	def save(self):
		comment_instance = models.usercomments()
		comment_instance.commenttext = self.cleaned_data["comment_field"]
		comment_instance.save()
		return comment_instance

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(label="Email", required = True)

	class Meta:
		model = User
		fields = ("username","email","password1","password2")

	def save(self,commit=True):
		user = super(RegistrationForm,self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user
