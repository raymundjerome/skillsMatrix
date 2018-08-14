from django.conf.urls import url
from . import views

app_name = 'skillsMatrixApp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'employee/$', views.employeeList.as_view(), name='employee-list'),
    url(r'employee/add/$', views.employeeCreate.as_view(), name='employee-add'),
    url(r'employee/(?P<pk>[0-9]+)/$', views.employeeUpdate.as_view(), name='employee-update'),
    url(r'employee/(?P<pk>[0-9]+)/delete/$', views.employeeDelete.as_view(), name='employee-delete'),

    url(r'skills/$', views.skillsList.as_view(), name='skills-list'),
    url(r'skills/add/$', views.skillsCreate.as_view(), name='skills-add'),
    url(r'skills/(?P<pk>[0-9]+)/$', views.skillsUpdate.as_view(), name='skills-update'),
    url(r'skills/(?P<pk>[0-9]+)/delete/$', views.skillsDelete.as_view(), name='skills-delete'),

    url(r'skills-matrix/$', views.skillsMatrixView.as_view(), name='skills-matrix'),
    url(r'skills-matrix/add/$', views.skillsMatrixCreate.as_view(), name='skills-matrix-add'),
    url(r'skills-matrix/(?P<pk>[0-9]+)/$', views.skillsMatrixUpdate.as_view(), name='skills-matrix-update'),
    url(r'skills-matrix/(?P<pk>[0-9]+)/delete/$', views.skillsMatrixDelete.as_view(), name='skills-matrix-delete'),
]
