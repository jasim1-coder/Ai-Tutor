from django.shortcuts import render
from . utils import get_ai_response
# Create your views here.

def index(request):
    response_text = ""
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response_text= get_ai_response(user_input)

    return render(request, 'tutor/index.html', {'response':response_text})