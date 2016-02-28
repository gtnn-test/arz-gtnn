from django.shortcuts import render, redirect
from gb.models import record

# Create your views here.
def gb(request):
    rec = record.objects.all();
    args = {'rec':rec}
    return render(request, 'gb.html', args)

def send (request):
    r_title = None
    r_text = None

    if 'title' in request.POST:
        r_title = request.POST['title']
    if 'text' in request.POST:
        r_text = request.POST['text']

    if r_title and r_text:
        new_record = record(title=r_title, text=r_text)
        new_record.save()

#    rec = record.objects.all();
#    args = {'rec':rec}
#    return render(request, 'gb.html', args)
    return redirect('/gb/')