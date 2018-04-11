# Generated by Django 2.0.2 on 2018-04-11 15:17

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import server.apps.sans.biosans.models
import server.apps.sans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_remote_submission', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioSANSConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('absolute_scale_factor', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('solid_angle_correction', models.CharField(blank=True, choices=[('', 'None'), ('detector_tubes=False, detector_wing=False', 'Regular'), ('detector_tubes=Tubes, detector_wing=False', 'Tubes'), ('detector_tubes=False, detector_wing=True', 'Wing')], default='', max_length=50, null=True)),
                ('normalization', models.CharField(choices=[('NoNormalization()', 'None'), ('TimeNormalization()', 'Time'), ('MonitorNormalization()', 'Monitor')], default='MonitorNormalization()', max_length=50)),
                ('iqxqy_nbins', models.IntegerField(default=80, verbose_name='Number of bins for I(Qx, Qy) calculation')),
                ('mask_component_name', models.CharField(choices=[('detector1', 'Main'), ('wing_detector', 'Wing')], default='detector1', help_text='The number of pixels masked are relative to this component', max_length=50, verbose_name='Component to mask')),
                ('mask_left', models.IntegerField(default=0, help_text='Number of pixels masked on the left of the detector (nx_low)', verbose_name='Left')),
                ('mask_right', models.IntegerField(default=0, help_text='Number of pixels masked on the right of the detector (nx_high)', verbose_name='Right')),
                ('mask_top', models.IntegerField(default=10, help_text='Number of pixels masked on the top of the detector (ny_high)', verbose_name='Top')),
                ('mask_bottom', models.IntegerField(default=10, help_text='Number of pixels masked on the bottom of the detector (ny_low)', verbose_name='Bottom')),
                ('mask_total_component_name', models.CharField(choices=[('detector1', 'Main'), ('wing_detector', 'Wing')], default='wing_detector', help_text='Totally masks this component. The name should be different from above!', max_length=50, verbose_name='Remove this component from reduction')),
                ('flood_file', models.CharField(help_text='File path', max_length=256, verbose_name='Sensitivity correction: Flood Data')),
                ('sensitivity_min', models.DecimalField(decimal_places=2, default=0.3, max_digits=10)),
                ('sensitivity_max', models.DecimalField(decimal_places=2, default=1.7, max_digits=10)),
                ('sensitivity_use_sample_dc', models.BooleanField(default=False, help_text='If use_sample_dc is set to True, the dark current data that was chosen to         be subtracted from the sample data will also be         subtracted from the flood data. The subtraction is done before the sensitivity is calculated.         Alternatively, a different file can be selected by specifying the dark_current parameter.', verbose_name='Use Sample Dark Current dor sensitivity')),
                ('dark_current_file', models.CharField(help_text='File path', max_length=256, verbose_name='Dark current')),
                ('transmission_beam_radius', models.DecimalField(decimal_places=2, default=3.0, max_digits=10)),
                ('transmission_theta_dependent', models.BooleanField(default=False, help_text='If set to False, the transmission correction will be applied by dividing         each pixel by the zero-angle transmission, without theta dependence.', verbose_name='Theta Dependent Transmission')),
                ('transmission_use_sample_dc', models.BooleanField(default=False, help_text='If this is set to True, the dark current data that was chosen to be         subtracted from the sample data will also be subtracted from the flood data.', verbose_name='Use Sample Dark Current for Transmission')),
                ('azimuthal_average_binning', models.CharField(help_text="Select a Q range of the form: 'min,-step,max'.             Note that negtive step means log binning.", max_length=128, validators=[server.apps.sans.biosans.models.validate_q_range], verbose_name='Q range')),
                ('empty_beam_file', models.CharField(blank=True, help_text='Note that the user can always overwrite this value!', max_length=256, verbose_name='Empty Beam Transmission file')),
                ('beam_center_file', models.CharField(blank=True, help_text='Note that the user can always overwrite this value!', max_length=256, verbose_name='Beam Center file')),
                ('save_iq', models.BooleanField(default=False, help_text='If selected will save on dist the IQ curve. Usefull for         posterior feetings / stitching.', verbose_name='Save IQ data as file')),
                ('stiching_q_min', models.DecimalField(blank=True, decimal_places=5, help_text='Value only used for stiching. Only use for High Q Region.', max_digits=10, null=True, verbose_name='Stiching Q min')),
                ('stiching_q_max', models.DecimalField(blank=True, decimal_places=5, help_text='Value only used for stiching. Only use for Low Q Region.', max_digits=10, null=True, verbose_name='Stiching Q max')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biosansconfiguration_instruments', related_query_name='biosansconfiguration_instrument', to='catalog.Instrument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biosansconfiguration_users', related_query_name='biosansconfiguration_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='BioSANSReduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script_execution_path', models.CharField(max_length=256)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.         If the script was generated already just shows it!')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biosansreduction_instruments', related_query_name='biosansreduction_instrument', to='catalog.Instrument')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biosansreduction_job', related_query_name='biosansreduction_job', to='django_remote_submission.Job')),
                ('script_interpreter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biosansreduction_interpreters', related_query_name='biosansreduction_interpreter', to='django_remote_submission.Interpreter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biosansreduction_users', related_query_name='biosansreduction_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='BioSANSRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_beam_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Empty Beam Transmission')),
                ('beam_center_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Beam Center')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('entries', django.contrib.postgres.fields.jsonb.JSONField()),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='sans.BioSANSConfiguration')),
                ('reduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='sans.BioSANSReduction')),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='GPSANSConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('wavelength', models.DecimalField(blank=True, decimal_places=2, help_text='If empty uses the value set in the data file.', max_digits=4, null=True, verbose_name='Wavelength (Å)')),
                ('wavelength_spread', models.DecimalField(blank=True, decimal_places=2, help_text='If empty uses the value set in the data file.', max_digits=3, null=True, verbose_name='Wavelength Spread (%)')),
                ('sample_detector_distance', models.DecimalField(blank=True, decimal_places=3, help_text='(in meters) If empty uses the value set in the data file.', max_digits=5, null=True, verbose_name='Sample Detector Distance (m)')),
                ('solid_angle_correction', models.CharField(blank=True, choices=[('', 'None'), ('detector_tubes=False, detector_wing=False', 'Regular'), ('detector_tubes=Tubes, detector_wing=False', 'Tubes')], default='', max_length=50)),
                ('absolute_scale_factor', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('normalization', models.CharField(choices=[('NoNormalization()', 'None'), ('TimeNormalization()', 'Time'), ('MonitorNormalization()', 'Monitor')], default='MonitorNormalization()', max_length=50)),
                ('dark_current_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sample_aperture_diameter', models.DecimalField(decimal_places=2, default=10.0, max_digits=10)),
                ('direct_beam_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('mask_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sensitivity_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sensitivity_min', models.DecimalField(decimal_places=2, default=0.4, max_digits=10)),
                ('sensitivity_max', models.DecimalField(decimal_places=2, default=2.0, max_digits=10)),
                ('empty_beam_file', models.CharField(blank=True, help_text='Note that the user can always overwrite this value!', max_length=256, verbose_name='Empty Beam Transmission file')),
                ('beam_center_file', models.CharField(blank=True, help_text='Note that the user can always overwrite this value!', max_length=256, verbose_name='Beam Center file')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpsansconfiguration_instruments', related_query_name='gpsansconfiguration_instrument', to='catalog.Instrument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpsansconfiguration_users', related_query_name='gpsansconfiguration_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='GPSANSReduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script_execution_path', models.CharField(max_length=256)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.         If the script was generated already just shows it!')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpsansreduction_instruments', related_query_name='gpsansreduction_instrument', to='catalog.Instrument')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gpsansreduction_job', related_query_name='gpsansreduction_job', to='django_remote_submission.Job')),
                ('script_interpreter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gpsansreduction_interpreters', related_query_name='gpsansreduction_interpreter', to='django_remote_submission.Interpreter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpsansreduction_users', related_query_name='gpsansreduction_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='GPSANSRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_beam_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Empty Beam Transmission')),
                ('beam_center_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Beam Center')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('entries', django.contrib.postgres.fields.jsonb.JSONField()),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='sans.GPSANSConfiguration')),
                ('reduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='sans.GPSANSReduction')),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
    ]
