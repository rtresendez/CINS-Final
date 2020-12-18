from django.db.models.fields import PositiveIntegerField
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import UpdateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import csv
import json


from .import models
from . import forms
import chat

def index(request):
    title = "My website"
    content = "Hello CINS465"
    context = {
        "title":title,
        "body":content,
    }
    return render(request,"base.html",context=context)


def get_data(request):
    data = {
        "sales": 10000,
        "customers": 10,
    }
    return JsonResponse(data)

@login_required(login_url='/login/')

def chartView(request):

    title = "Chart Viewing Page"
    context = {
        "title":title,
    }
    return render(request,"chartSpace.html",context=context)



def get_stories(request):
    story_objects = models.Story_Model.objects.all()
    # {"key":value,"key":["value","value"], "key3":{}}
    story_list = {}
    story_list["story"]=[]
    for st in story_objects:
        story_list["story"]+=[st.story]
    return JsonResponse(story_list)

def registerView(request):
    if request.method == "POST":
        form_instance = forms.userRegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.userRegistrationForm()
    context = {
        "form":form_instance,
    }

    return render(request,"registration/register.html", context =context)



def logoutView(request):
    logout(request)
    return redirect("/login/")

# @login_required(login_url='/login/')
# def form_view(request):
#     if request.method == "POST":
#         story_form = forms.Story_generator_form(request.POST)
#         if story_form.is_valid():
#             story_form.save()
#             story_form = forms.Story_generator_form()
#             return redirect(form_view)
#     else:
#         story_form = forms.Story_generator_form()
#     story_form = forms.Story_generator_form()
#     story = models.Story_Model.objects.all()
#     title = "Site with Dynamic Refreshing!"
#     context = {
#         "title":title,
#         "story":story,
#         "form":story_form,
#     }
#     return render(request,"forms.html",context = context)

@login_required(login_url='/login/')
def roomView(request):
    if request.method == "POST" and (request.POST.get("room-submit", "") 
        == "Create Room"):
        room_form = forms.chartRoomForm(request.POST, request.FILES)
        if room_form.is_valid():
            room_form.save(request)
            room = room_form.cleaned_data["roomName"]
            room_form = forms.chartRoomForm()
            return redirect(chartView(room))
        else:
            print(room_form.errors)
    else:
        room_form = forms.chartRoomForm()
    room_form = forms.chartRoomForm()
    title = "Make a room"
    form = room_form
    context = {
        "title":title,
        "form":form,
    }
    return render(request,"rooms.html",context = context)



@login_required(login_url='/login/')
def chartBuilderView(request):
    if request.method == "POST" and (request.POST.get("build-form", "") 
        == "Make Chart"):
        chart_form = forms.chartSpecForm(request.POST)
        if chart_form.is_valid():
            chart_form.save(request)
            chart_form = forms.chartSpecForm()
            return redirect("/test2/")
        else:
            print (chart_form.errors)
            print (chart_form.error_class)
    else:
        chart_form = forms.chartSpecForm()
    chart_form = forms.chartSpecForm()
    title = "Chart Builder"
    form = chart_form
    context = {
        "title":title,
        "form":form,
    }
    return render(request,"test.html",context=context)