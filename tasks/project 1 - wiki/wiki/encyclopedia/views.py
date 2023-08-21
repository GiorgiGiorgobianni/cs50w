from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
from . import util
from markdown2 import Markdown
import random



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
    
def randomEntry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return HttpResponseRedirect(reverse("title",kwargs={"title":random_entry}))
    
 

    

