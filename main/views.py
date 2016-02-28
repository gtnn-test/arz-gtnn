from django.shortcuts import render

# Create your views here.
def hello(request):
    args = {'user':'Давыдов', 'dol':'Инженер-электроник'}
    return render(request, 'main.html', args)