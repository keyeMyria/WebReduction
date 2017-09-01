from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    # Common to HFIR and SNS
    url(r'^$', views.Instruments.as_view(), name='list_instruments'),
    url(r'^(?P<instrument>[\w\-]+)/$',
        cache_page(60*60)(views.IPTSs.as_view()), name='list_iptss'),
    url(r'^(?P<instrument>[\w\-]+)/(?P<ipts>[\w\-\.]+)/$',
        views.Runs.as_view(), name='list_runs'),

    # HFIR has exp field
    url(r'^(?P<instrument>[\w\-]+)/(?P<ipts>[\w\-\.]+)/(?P<exp>exp[\d]+)/$',
        views.Runs.as_view(), name='list_runs'),
    url(r'^(?P<instrument>[\w\-]+)/(?P<ipts>[\w\-\.]+)/(?P<exp>exp[\d]+)/(?P<filename>/HFIR/[^\.]+\.[A-Za-z]{3})/$',
        views.RunDetail.as_view(), name='run_detail'),
]
