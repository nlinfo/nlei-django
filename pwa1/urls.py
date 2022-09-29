# from django.conf.urls import url deprecated
from django.urls import re_path

from .views import manifest, service_worker, offline

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    re_path(r'^serviceworker\.js$', service_worker, name='serviceworker'),
    re_path(r'^manifest\.json$', manifest, name='manifest'),
    re_path(r'^offline/$', offline, name='offline')

    # these one are deprecated
    # url(r'^serviceworker\.js$', service_worker, name='serviceworker'),
    # url(r'^manifest\.json$', manifest, name='manifest'),
    # url('^offline/$', offline, name='offline')
]
