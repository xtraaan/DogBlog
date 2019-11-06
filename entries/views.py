from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView
from .models import Entry
from dog.models import Dog
# Create your views here.

def Home(request):
    entry_parker = Entry.objects.filter(dog__dog_name="Parker").order_by('-date')
    parker = Dog.objects.filter(dog_name="Parker")
    paginator = Paginator(entry_parker, 3)
    page = request.GET.get('page')
    entries = paginator.get_page(page)


    # entry_jaxon = Entry.objects.filter(dog__dog_name="Jaxon").order_by('-date')
    # jaxon = Dog.objects.filter(dog_name="Jaxon")
    # paginator2 = Paginator(entry_jaxon, 3)
    # page = request.GET.get('page')
    # j_entries = paginator.get_page(page)



    return render_to_response('entries/index.html',{'entries':entries,'parker':parker})

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['title', 'description', 'image', 'owner', 'dog']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)