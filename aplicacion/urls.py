from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from aplicacion import views, errorViews

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^course/$', views.CourseList.as_view()),
    #url(r'^course/(?P[0-9]+)/$', views.CourseList.as_view()),
    #url(r'^take/(?P[0-9]+)/$', views.TakeList.as_view()),
    url(r'^tomados/$', views.TakeList.as_view()),
    url(r'^error/$', errorViews.noEncontrado),
]

urlpatterns = format_suffix_patterns(urlpatterns)
