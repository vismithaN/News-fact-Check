from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    input_text = request.GET.get('input_text', '')

    # Example processing (you can modify this logic as needed)
    output_text = f"You entered: {input_text}"

    return render(request, 'index.html', {'output_text': output_text})
