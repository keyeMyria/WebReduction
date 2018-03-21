import re

from django.core.exceptions import ValidationError
from django.db import models

from server.apps.configuration.models import (Configuration,
                                              SansHfirGpsansConfiguration)

from server.apps.configuration.models import abstract

from .sans import SansRegion


class Reduction(abstract.Reduction):

    @models.permalink
    def get_absolute_url(self):
        return ('reduction:reduction_detail', [self.pk])


class (SansRegion):
    # We can not have ForeignKey for abstract models. It has to be here!!

    reduction = models.ForeignKey(SansHfirGpsansReduction,
                                  on_delete=models.CASCADE,
                                  related_name="regions",
                                  related_query_name="region",)

    configuration = models.ForeignKey(SansHfirGpsansConfiguration,
                                      on_delete=models.CASCADE,
                                      related_name="regions",
                                      related_query_name="region")

    def __str__(self):
        return "Reduction {}".format(self.reduction.title)