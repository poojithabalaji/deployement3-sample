from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView, CreateView,
                                    UpdateView, DeleteView,FormView)
from mycbvapp.models import student
# Create your views here.
class indexview(TemplateView):
    template_name ='homepage.html'


class studentListView(ListView):
    context_object_name ='students'
    model = student
    # template_name ='student_list.html'


class studentDetailView(DetailView):
    context_object_name ='studentdetail'
    model = student
    template_name ="mycbvapp/student_detail.html"

#class studentCreateView(CreateView):

class studentCreateView(CreateView):
    model = student
    fields = ['name','school','age']

class studentUpdateView(UpdateView):
    model =student
    fields =['age','school']
    template_name_suffix = '_update_form'

class studentDeleteView(DeleteView):
    model =student
    success_url =reverse_lazy('mycbvapp:list')
