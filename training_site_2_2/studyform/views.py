# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

# def index(request):
#
#     template = loader.get_template('studyform/index.html')
#     context = {
#         'latest_question_list': 'latest_question_list,'
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    return render(request, 'studyform/name.html', {'form': form})
def postresult(request):
    # return HttpResponse(request.POST['1'])
    return HttpResponse(request.POST['your_name'])