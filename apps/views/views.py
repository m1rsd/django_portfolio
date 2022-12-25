from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView

from apps.forms import ContactForm
from apps.models import Skills, Facts, Education, ProfessionalExperience, Services, Testimonials, User, Project, \
    Portfolio, Photo


# Create your views here.

class IndexView(FormView):
    template_name = 'apps/index.html'
    model = User
    form_class = ContactForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        skills = Skills.objects.all()
        result = []
        if Skills.objects.count() > 3:
            for i in range(skills.count() // 3 + 1):
                result.append(skills[:3])
                skills = skills[3:]
        else:
            result.append(skills)

        context['skills'] = result
        context['user'] = User.objects.all().first()
        context['facts'] = Facts.objects.first()
        context['education'] = Education.objects.first()
        context['experience'] = ProfessionalExperience.objects.all()
        context['services'] = Services.objects.all()
        context['testimonials'] = Testimonials.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("../")


class ProjectDetailView(DetailView):
    template_name = 'apps/portfolio-details.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.first()
        context['project'] = self.get_object()
        context['photos'] = Photo.objects.filter(project_id=self.get_object())
        return context
