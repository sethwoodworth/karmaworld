from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView

from karmaworld.apps.courses.models import Course
from karmaworld.apps.courses.views import CourseDetailView

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^/b/(?P<slug>[^/]+)$', CourseDetailView.as_view(), name='course_detail'),

    url(r'^$', ListView.as_view(model=Course), name='home'),
)
