from django.views import generic
from .models import employee, organization, skills, skillsMatrix
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = 'skillsMatrixApp/index.html'

    # context_object_name = 'all_employee'

    # def get_queryset(self):
    #  return employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_employee'] = employee.objects.all()
        context['all_skills'] = skills.objects.all().order_by('dateModified').reverse()
        context['all_skillsMatrix'] = skillsMatrix.objects.all()
        return context


class DetailView(generic.DetailView):
    model = employee
    template_name = 'skillsMatrixApp/detail.html'


class employeeList(generic.ListView):
    template_name = 'skillsMatrixApp/employee-list.html'
    context_object_name = 'employeeList'

    def get_queryset(self):
        return employee.objects.all()


class employeeCreate(SuccessMessageMixin, CreateView):
    model = employee
    fields = ['firstName', 'lastName', 'role']

    success_url = reverse_lazy('skillsMatrixApp:employee-list')
    success_message = "Employee added successfully."

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('skillsMatrixApp:index'))
        return super(employeeCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        if "another" in self.request.POST:
            return reverse('skillsMatrixApp:employee-add')
        # else return the default `success_url`
        return super(employeeCreate, self).get_success_url()


class employeeUpdate(UpdateView):
    model = employee
    fields = ['firstName', 'lastName', 'role']

    success_url = reverse_lazy('skillsMatrixApp:employee-list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            self.object = self.get_object()
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(employeeUpdate, self).post(request, *args, **kwargs)


class employeeDelete(DeleteView):
    model = employee
    success_url = reverse_lazy('skillsMatrixApp:employee-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(employeeDelete, self).post(request, *args, **kwargs)


class skillsList(generic.ListView):
    template_name = 'skillsMatrixApp/skills-list.html'
    context_object_name = 'skillsList'

    def get_queryset(self):
        return skills.objects.all()


class skillsCreate(SuccessMessageMixin, CreateView):
    model = skills
    fields = ['skillName', 'technology', 'description', 'lastModifiedByID']

    success_url = reverse_lazy('skillsMatrixApp:skills-list')
    success_message = "Skill added successfully."

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('skillsMatrixApp:index'))
        return super(skillsCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        if "another" in self.request.POST:
            return reverse('skillsMatrixApp:skills-add')
        # else return the default `success_url`
        return super(skillsCreate, self).get_success_url()

class skillsUpdate(UpdateView):
    model = skills
    fields = ['skillName', 'technology', 'description', 'lastModifiedByID']

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            self.object = self.get_object()
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(skillsUpdate, self).post(request, *args, **kwargs)


class skillsDelete(DeleteView):
    model = skills
    success_url = reverse_lazy('skillsMatrixApp:skills-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(skillsDelete, self).post(request, *args, **kwargs)


class skillsMatrixView(generic.ListView):
    template_name = 'skillsMatrixApp/skills-matrix.html'
    context_object_name = 'skillsMatrix'

    def get_queryset(self):
        return skillsMatrix.objects.all()


class skillsMatrixCreate(SuccessMessageMixin, CreateView):
    model = skillsMatrix
    fields = ['skillsMatrixEmployee', 'skillsMatrixSkills', 'proficiency', 'levelOfInterest']

    success_url = reverse_lazy('skillsMatrixApp:skills-matrix')
    success_message = "Skill associated to Employee successfully."

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('skillsMatrixApp:index'))
        return super(skillsMatrixCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        if "another" in self.request.POST:
            return reverse('skillsMatrixApp:skills-matrix-add')
        # else return the default `success_url`
        return super(skillsMatrixCreate, self).get_success_url()



class skillsMatrixUpdate(UpdateView):
    model = skillsMatrix
    fields = ['skillsMatrixEmployee', 'skillsMatrixSkills', 'proficiency', 'levelOfInterest']

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            self.object = self.get_object()
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(skillsMatrixUpdate, self).post(request, *args, **kwargs)


class skillsMatrixDelete(DeleteView):
    model = skillsMatrix
    success_url = reverse_lazy('skillsMatrixApp:skills-matrix')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(skillsMatrixDelete, self).post(request, *args, **kwargs)
