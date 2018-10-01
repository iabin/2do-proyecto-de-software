from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from aplicacion import views, errorViews

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^index/$', views.index, name='index'),
    url(r'^course/$', views.CourseList.as_view()),
    url(r'^busca/$', views.busca,name='busca'),

    #url(r'^users/(?P<format>[a-z0-9]+)/$', views.UserDetail.as_view()),
    #path(r'^take/(?P[0-9]+)/$', views.TakeList.as_view()),
    url(r'^tomados/$', views.TakeList.as_view()),

    url(r'^', errorViews.noEncontrado),

]

urlpatterns = format_suffix_patterns(urlpatterns)
