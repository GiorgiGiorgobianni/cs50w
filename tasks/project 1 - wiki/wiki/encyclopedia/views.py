from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from django.urls import reverse
from random import choice

class MyForm(forms.Form):
    textInput = forms.CharField(label="text",required= False,
    widget= forms.TextInput
    )

form = MyForm()

class NewPageForm(forms.Form):
    pagename = forms.CharField(label="Title",required = True,
    widget= forms.TextInput
    (attrs={'placeholder':'Enter Title','style':'top:2rem, bottom:1rem'}))

    body = forms.CharField(label="Markdown content",required= False, 
    widget= forms.Textarea
    (attrs={'placeholder':'Enter markdown content','style':'top:2rem, width:20px, '}))



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryScreen(request, title):
    
    screen = util.get_entry(title)

    return render(request, "encyclopedia/entryScreen.html", {
        "title":title,
        "content":screen,
        
    })

def searchEntries(request):
    query = request.GET.get('q', '')
    if util.get_entry(query) != None:
        return HttpResponseRedirect(reverse("title", kwargs={
            "title": query,
        }))
    else:
        titleSubstrings = []
        for entry in util.list_entries():
            if query.lower() in entry.lower():
                titleSubstrings.append(entry)

    return render(request, "encyclopedia/index.html", {
        "entries": titleSubstrings,
        "search": True ,
        "query": query,
    })

def newEntry(request):
    if request.method == 'GET':
        create_form = NewPageForm()
        return render(request, "encyclopedia/createEntry.html", {
            "form":form,
            "create_form": create_form,
        })
    
    else:
        create_form = NewPageForm(request.POST)
        if create_form.is_valid():

            title = create_form.cleaned_data["pagename"]
            body = create_form.cleaned_data["body"]

            all_entries = util.list_entries()
            for filename in all_entries:
                if title.lower() == filename.lower():
                    create_form = NewPageForm()
                    error_message = "This title is already in use, try another one"
                    
                    return render(request, "encyclopedia/createEntry.html", {
                        "form":form,
                        "create_form":create_form,
                        "error":error_message
                    })
            util.save_entry(title, body)
            return entryScreen(request, title)
        
        else:

            return render(request, "encyclopedia/createEntry.html", {
                "form":form,
                "create_form":create_form
            })

def editEntry(request, entry):
    content = util.get_entry(entry)
    if content is None :
        return render(request, "encyclopedia/pageNotFound.html", {
            "entryTitle":entry
        })
    else:
        form = NewPageForm()
        form.fields["title"] = entry
        
    
def saveEdit(request):
    edit_form = forms.EditPageForm(request.post)
    
    if edit_form.is_valid():
        entry = edit_form.cleaned_data["entry"]
        details = edit_form.cleaned_data["body"]

        save_entry = util.save_entry(entry,details)

        return entryScreen(request,entry)
    else:
        return render(request, "encyclopedia/editEntry.html", {
            "form":form,
            "edit_form":edit_form,
        })

def randomEntry(request):
    all_entries = util.list_entries()
    random_entry = choice(all_entries)
    return render(request, "encyclopedia/randomEntry.html",{
        "random_entry":random_entry,
    })
