import re
import os
import random

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import Http404



def list_entries(query):
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    lower_filename = [filename.lower() for filename in filenames]
    print(lower_filename)
    search_results = []


    if query == "":
        return list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))

    else:


        for filename in lower_filename:


            if filename.endswith(".md"):
                match = filename.find(query)
                if match == -1:
                    print(f"No match for " + filename)
                else:
                    search_result = filename
                    search_results.append(search_result)
                    print("match for " + filename)






        print(search_results)
        return list(sorted(re.sub(r"\.md$", "", filename) for filename in search_results ))



def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    NewContent = "#{} \n \n {}".format(title, content)
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(NewContent))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
#    try:
    f = default_storage.open(f"entries/{title}.md")
    return f.read().decode("utf-8")
#    except FileNotFoundError:
#        raise Http404("Page doesn't exist D:")
