##########################################################################
# GPSANS
##########################################################################

from django.core.exceptions import ValidationError
from django.db import models

from server.apps.configuration.models import abstract

# I'm naming this as this prefix because I cannot have 2 tables with the same name
# See __init__.py . They are called Configuration in the end.
class ConfigurationGPSANS(abstract.Configuration):

    wavelength = models.DecimalField(
        u'Wavelength (\u212B)',
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text= "If empty uses the value set in the data file."
    )

    wavelength_spread = models.DecimalField(
        'Wavelength Spread (%)',
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="If empty uses the value set in the data file."
    )

    sample_detector_distance = models.DecimalField(
        'Sample Detector Distance (m)',
        max_digits=5,
        decimal_places=3,
        blank=True,
        null=True,
        help_text="(in meters) If empty uses the value set in the data file."
    )

    SOLID_ANGLE_CHOICES = (
        ("", "None"),
        ("detector_tubes=False, detector_wing=False", "Regular"),
        ("detector_tubes=Tubes, detector_wing=False", "Tubes"),
    )

    solid_angle_correction = models.CharField(
        max_length=50,
        blank=True,
        choices=SOLID_ANGLE_CHOICES,
        default=SOLID_ANGLE_CHOICES[0][0],
    )

    absolute_scale_factor = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1.0
    )

    NORMALIZATION_CHOICES = (
        ("NoNormalization()", "None"),
        ("TimeNormalization()", "Time"),
        ("MonitorNormalization()", "Monitor"),
    )

    normalization = models.CharField(
        max_length=50,
        choices=NORMALIZATION_CHOICES,
        default=NORMALIZATION_CHOICES[2][0],
    )

    dark_current_file = models.CharField(
        max_length=256,
        blank=True,
        help_text="File path"
    )

    sample_aperture_diameter = models.DecimalField(
        max_digits=10, decimal_places=2, default=10.0)

    direct_beam_file = models.CharField(
        max_length=256, blank=True, help_text="File path")
    mask_file = models.CharField(
        max_length=256, blank=True, help_text="File path")

    sensitivity_file = models.CharField(
        max_length=256, blank=True, help_text="File path")

    sensitivity_min = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.4)
    sensitivity_max = models.DecimalField(
        max_digits=10, decimal_places=2, default=2.0)

    empty_beam_file = models.CharField(
        "Empty Beam Transmission file",
        max_length=256,
        blank=True,
        help_text="Note that the user can always overwrite this value!"
    )

    beam_center_file = models.CharField(
        "Beam Center file",
        max_length=256,
        blank=True,
        help_text="Note that the user can always overwrite this value!"
    )

    @models.permalink
    def get_absolute_url(self):
        return ('sans:detail', [self.pk])

    class Meta:
        verbose_name = "Configuration GPSANS"
        verbose_name_plural = "Configuration GPSANSs"