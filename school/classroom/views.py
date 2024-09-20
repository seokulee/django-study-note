from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView

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