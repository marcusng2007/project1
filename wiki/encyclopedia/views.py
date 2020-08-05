from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls import reverse
import markdown2

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")


def index(request):

#    viewpage = util.get_entry("Django")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        #So this lists all entries in the wiki
        #It doesn't do anything else

        #"page": markdown2.markdown(viewpage)

    })

def entry(request, title):

    viewpage = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {

        "content": markdown2.markdown(viewpage),
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
