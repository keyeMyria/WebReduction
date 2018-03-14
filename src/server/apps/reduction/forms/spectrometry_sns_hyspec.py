import logging

from django.forms import ModelForm, inlineformset_factory

from server.apps.configuration.models import SpectrometrySnsHyspecConfiguration

from ..forms import ReductionForm, ReductionScriptForm, RegionForm
from ..models import SpectrometrySnsHyspecReduction, SpectrometrySnsHyspecRegion

logger = logging.getLogger(__name__)  # pylint: disable=C0103


class SpectrometrySnsHyspecReductionForm(ReductionForm, ModelForm):
    class Meta(ReductionForm.Meta):
        model = SpectrometrySnsHyspecReduction


class SpectrometrySnsHyspecReductionScriptForm(ReductionScriptForm, ModelForm):
    class Meta(ReductionScriptForm.Meta):
        model = SpectrometrySnsHyspecReduction


class SpectrometrySnsHyspecRegionForm(RegionForm, ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpectrometrySnsHyspecRegionForm, self).__init__(*args, **kwargs)
        # self.helper.add_layout(
        #     Field('DELETE', css_class='input-small'),
        # )

    class Meta(RegionForm.Meta):
        model = SpectrometrySnsHyspecRegion


# New
SpectrometrySnsHyspecRegionInlineFormSetCreate = inlineformset_factory(
    SpectrometrySnsHyspecReduction,
    SpectrometrySnsHyspecRegion,
    form=SpectrometrySnsHyspecRegionForm,
    extra=3,
    can_delete=True
)
# Edit
SpectrometrySnsHyspecRegionInlineFormSetUpdate = inlineformset_factory(
    SpectrometrySnsHyspecReduction,
    SpectrometrySnsHyspecRegion,
    form=SpectrometrySnsHyspecRegionForm,
    extra=0,
    can_delete=True)
