from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import TextFile
from .tools import calculate_tf, calculate_idf
import re


class UploadFile(CreateView):
    model = TextFile
    fields = ['file']
    template_name = 'text_reader/upload.html'

    def form_valid(self, form):
        text_file = form.save(commit=False)
        text_file.save()
        return redirect('show_words', text_file_id=text_file.id)


def show_words(request, text_file_id):
    text_file = TextFile.objects.get(id=text_file_id)
    with open(text_file.file.path, 'r', encoding='utf-8') as file:
        input_string = file.read().lower()
        words = re.sub(r'[^\w\s]', '', input_string)
        idf = calculate_idf(words)
        tf = calculate_tf(words)
    context = [{'word': word, 'tf': tf[word], 'idf': idf.get(word, 0)} for word in tf]
    context_sort = sorted(context, key=lambda x: x['idf'], reverse=True)
    return render(request, 'text_reader/text_reader.html', {'context': context_sort})
