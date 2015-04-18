from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'projects.views.index', name='index'),
    url(r'^dev$', 'projects.views.development', name='dev'),
    url(r'^security$', 'projects.views.security', name='security'),
    url(r'^hobby$', 'projects.views.hobby', name='hobby'),
    # url(r'^projects/', include('projects.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
