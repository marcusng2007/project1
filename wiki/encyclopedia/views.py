from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls import reverse
import random

from markdown2 import Markdown

from . import util

markdowner = Markdown()

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")

class EditForm(forms.Form):
    textarea = forms.CharField(label="textarea", required=False)

def index(request):

#    viewpage = util.get_entry("Django")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(""),
        #So this lists all entries in the wiki
        #It doesn't do anything else

        #"page": markdown2.markdown(viewpage)

    })

def entry(request, title):

    viewpage = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {

        "content": markdowner.convert(viewpage),
        "title": title
    })


def create(request):
#    viewpage = util.get_entry("Django")
    form = NewEntryForm(request.POST)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

#        form = NewEntryForm(request.POST)
        if form.is_valid():
            util.save_entry(title, content)

            return HttpResponseRedirect('/')

        else:
            form: NewEntryForm()


#        return render(request, "encyclopedia/create.html", {'entry_form': form})

    return render(request, "encyclopedia/create.html", {'entry_form': form})



def search(request):

    q = request.GET.get('q').strip()
    print(q)

    return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries(q),
        "q": q
    })


def edit(request, title):
    print(title)

    viewpage = util.get_entry(title)

    if request.method == 'GET':

        return render(request, "encyclopedia/edit.html", {

            "content": markdowner.convert(viewpage),
            "title": title
        })

    else:
        form = EditForm(request.POST)
        print(form)
        content = request.POST.get('content')
        if form.is_valid():
#            textarea = form.cleaned_data[content]
            util.save_entry(title, content)

            print(title)
            return HttpResponseRedirect('/')

        else:
            print("it didnt work")
            form: NewEntryForm()


#        return render(request, "encyclopedia/create.html", {'entry_form': form})

    return render(request, "encyclopedia/edit.html", {

        "content": markdowner.convert(viewpage),
        'title': title
    })




def random_page(request):
    entries = util.list_entries("")
    print(entries)
    selected_page = random.choice(entries)
    return redirect(f'entry/{selected_page}')
