from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView

from classroom.forms import ContactForm
from classroom.models import Teacher


# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


# Creating new Instance of Model
class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html (find template automatically)
    # .save()
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    model = Teacher
    # model_list.html
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teachers'


# RETURN ONLY ONE MODEL ENTRY PK
class TeacherDetailView(DetailView):
    model = Teacher
    # model_detail.html
    # PK -> {{ teacher }}


class TeacherUpdateView(UpdateView):
    model = Teacher
    # SHARE model_form.html
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')


# Form -> Confirm Delete Button
class TeacherDeleteView(DeleteView):
    model = Teacher
    # model_confirm_delete.html
    success_url = reverse_lazy('classroom:list_teacher')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL
    # TODO: 이 부분 더 정리하기!
    success_url = reverse_lazy('classroom:thank_you')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)