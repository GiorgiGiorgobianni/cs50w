from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
from . import util
from markdown2 import Markdown
import random
from . import forms




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryScreen(request,title):
    convert = Markdown()
    entryPage = util.get_entry(title)
    
    if entryPage is None:
        return render(request,"encyclopedia/notFoundScreen.html")
    
    return render(request, "encyclopedia/entryScreen.html", {
        "title":title,
        "entryContent":convert.convert(entryPage),
    })

def search(request):
    query = request.GET.get('q','')
    if(util.get_entry(query) is not None):
       return HttpResponseRedirect(reverse("title",kwargs={"title":query,}))
    else:
        entrySubString = []
        for entry in util.list_entries():
            if query.upper() in entry.upper():
                entrySubString.append(entry)
        return render(request, "encyclopedia/index.html", {
                "entries":entrySubString,
                "search":True,
                "query":query,
                
            })
    
def newEntry(request):
    if request.method == "POST":
        entry_form = forms.NewEntryForm(request.POST)
        if entry_form.is_valid():
            title = entry_form.cleaned_data["title"]
            content = entry_form.cleaned_data["content"]
            if(util.get_entry(title) is None or entry_form.cleaned_data["edit"] is True):
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("title", kwargs={"title":title}))
            else:
                return render(request, "encyclopedia/createEntryScreen.html", {
                    "entryForm":entry_form,
                    "exists":True,
                    "title":title,
                })
        else:
            return render(request, "encyclopedia/createEntryScreen.html", {
                    "entryForm":entry_form,
                    "exists":False,
                })
    else:
        return render(request, "encyclopedia/createEntryScreen.html", {
                    "entryForm":forms.NewEntryForm(),
                    "exists":False,
                })
    
def editEntry(request):
    title = request.POST.get("edit")
    print("title: ",title)
    content = util.get_entry(title)
    edit_form = forms.EditEntryForm(initial={"title":title, "content":content})
    if edit_form.is_valid():
        return render(request, "encyclopedia/editEntryScreen.html", {
            "title":title,
            "editForm":edit_form,
        })
    else:
        return render(request, "encyclopedia/editEntryScreen.html", {
            "title":title,
            "editForm":edit_form,
        })
                

def saveEntry(request):
    edit_form = forms.EditEntryForm(request.POST)
    if edit_form.is_valid():
        title = edit_form.cleaned_data["title"]
        content = edit_form.cleaned_data["content"]
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("title", kwargs={"title":title}))
    else:
        return render(request, "encyclopedia/editEntryScreen.html", {
            "title":title,
            "editForm":edit_form,
        })
            
    
def randomEntry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return HttpResponseRedirect(reverse("title",kwargs={"title":random_entry}))
    
 

    

