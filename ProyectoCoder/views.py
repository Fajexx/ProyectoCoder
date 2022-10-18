from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Course

def create_course(request, name: str = "course", code: int = 0):
    template = loader.get_template("template_course.html")