from django.http import HttpResponse
from django.shortcuts import render
from prompting import factCheck


def index(request):
    if 'input_text' in request.GET:
        input_text = request.GET['input_text']
        output_text=factCheck(input_text)

    else:
        output_text = None  # No output if nothing has been submitted

    return render(request, 'index.html', {'output_text': output_text})