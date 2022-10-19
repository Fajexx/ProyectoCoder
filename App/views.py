from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from App.models import Relative

def create_relative(request, name: str, age: int, birthday: date, relation_ship: str):
    template = loader.get_template('/Users/fabri/Desktop/proyectos-python/my_family/templates/template_family.html')
    relative = Relative(name=name, age=age, birthday=birthday, relation_ship=relation_ship)
    relative.save() #save into the DB
    context_dict = {"relative":relative}
    render = template.render(context_dict)
    return HttpResponse(render)
