from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
     # Configurations
    url(r'^$', JobsList.as_view(), name='job_list'),
    url(r'^(?P<pk>\d+)$', JobDetail.as_view(), name='job_detail'),
    url(r'^livelog/(?P<pk>\d+)$', JobLiveLog.as_view(), name='job_log_live'),
    url(r'^live$', TemplateView.as_view(template_name='results/job_live.html'), name='job_list_live'),
    url(r'^zipfiles$', ZipFilesView.as_view(), name='zipfiles'),

    # Cache for 60 * 15 seconds
    # url(r'^result/(?P<pk>\d+)/plot$', cache_page(60 * 15)(ResultPlot.as_view()), name='result_plot'),
]
