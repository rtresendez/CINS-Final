from django import forms
from random import randint
from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm

from . import models


VERB_CHOICES = (
    ("was","was"),
    ("is","is"),
    ("has","has"),
    ("had","had"),
    ("will","will"),
)

def email_validator(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email already being used.")
    return value

def username_validator(value):
    user = User.objects.filter(username=value)
    if len(user) > 0:
        raise forms.ValidationError("Username already being used.")
    return value


class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="email",
        required=True,
        validators=[email_validator],
    )

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self,commit=True):
        user = super(userRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class Story_generator_form(forms.Form):

    char_name = forms.CharField(
        label = "Character Name",
        required = True,
        max_length=240
        )
    Verb = forms.ChoiceField(
        choices=VERB_CHOICES
        )

    activity = forms.CharField(
        label = "Character's Activity",
        required = True,
        max_length=240
        )
    adjective = forms.CharField(
        label = "Provide an Adjective",
        required = True,
        max_length=240
        )


    def save(self):
        rand = randint(0,1)
        story_inst = models.Story_Model()
        if rand:
            story_inst.story = self.cleaned_data["char_name"] + " " + self.cleaned_data["Verb"] + " " + self.cleaned_data["adjective"] + " " +  self.cleaned_data["activity"] + "."
        else:
            story_inst.story = self.cleaned_data["char_name"] + " "  + self.cleaned_data["Verb"] + " " + self.cleaned_data["activity"] + " " + self.cleaned_data["adjective"] + "." 
        story_inst.save()
        return story_inst


class chartRoomForm(forms.Form):
    roomName = forms.CharField(
        label = "Enter a name for your room.",
        required=True,
        max_length=24,
    )
    upload_file = forms.FileField(
        label = "Submit the dataset you would like to view.",
        required = True,
    )

    def save(self, request):
        room_inst = models.chartRoomModel()
        room_inst.roomName = self.cleaned_data["roomName"]
        room_inst.user = request.user
        room_inst.upload_file = self.cleaned_data["upload_file"]
        room_inst.save()
        return room_inst