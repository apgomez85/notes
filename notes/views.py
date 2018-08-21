from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from .forms import EntryModelForm
from django.contrib import messages
# Create your views here.


def entry_list(request):
    all_entries = Entry.objects.all()
    context = {
        'object_list': all_entries
    }
    return render(request, 'notes/entries.html', context)


def entry_detail(request, id):
    note = get_object_or_404(Entry, id=id)
    context = {
        'object': note
    }
    return render(request, 'notes/entries_detail.html', context)


def entry_create(request):
    form = EntryModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        entry_id = form.instance.id
        entry = get_object_or_404(Entry, id=entry_id)
        messages.info(request, 'Created a New Note.')
        return redirect(entry.get_absolute_url())
    context = {
        'form': form
    }

    return render(request, 'notes/entries_create.html', context)


def entry_update(request, id):
    instance = get_object_or_404(Entry, id=id)
    form = EntryModelForm(request.POST or None,
                          request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        entry_id = form.instance.id
        entry = get_object_or_404(Entry, id=entry_id)
        return redirect(entry.get_absolute_url())
    context = {
        'form': form,
        'instance': 'object',
    }

    return render(request, 'notes/entries_update.html', context)
