from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Assignment

# Create your views here.

#def assignment_list(request):
#    assignments = Assignment.objects.all()
#    template = loader.get_template('assignment_list.html')
#    context = {
#        'assignments': assignments,
#    }
#    return HttpResponse(template.render(context,request))
