# Generated by Django 2.0.2 on 2018-04-11 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Facility name (e.g. "SNS" or "HFIR")', max_length=32, verbose_name='facility name')),
                ('description', models.CharField(help_text='Facility description (e.g. "Spallation Neutron Source")', max_length=1024, verbose_name='facility description')),
                ('visible', models.BooleanField(default=False, help_text='Whether the facility is visible in the dashboard', verbose_name='facility is visible')),
            ],
            options={
                'verbose_name_plural': 'Facilities',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Instrument name (e.g. "EQSANS" or "BioSANS")', max_length=32, verbose_name='instrument name')),
                ('description', models.CharField(help_text='Instrument description (e.g. "Backscattering Spectrometer")', max_length=256, verbose_name='instrument description')),
                ('beamline', models.CharField(help_text='Beamline that goes into instrument (e.g. "BL-2")', max_length=32, verbose_name='instrument beamline')),
                ('technique', models.CharField(blank=True, help_text='Instrument technique (e.g. "SANS", "TAS")', max_length=256, verbose_name='instrument technique')),
                ('catalog_name', models.CharField(help_text='Name used for querying ONCat server (e.g. "EQSANS")', max_length=32, verbose_name='instrument ONCat name')),
                ('ldap_group_name', models.CharField(help_text='Group name of the instrument team in the LDAP server (e.g. "sns_eqsans_team").', max_length=32, verbose_name='instrument ldap group name')),
                ('drive_path', models.CharField(help_text='Name used for loading files from shared filesystem', max_length=256, verbose_name='instrument drive path')),
                ('data_file_path_template', models.CharField(blank=True, help_text='Python template for the full path of the data files', max_length=512)),
                ('reduction_path_template', models.CharField(blank=True, help_text='Python template for the full path of the folder where the reduced files go', max_length=512)),
                ('visible_reduction', models.BooleanField(default=False, help_text='Whether the instrument can do reductions', verbose_name='instrument can do reductions')),
                ('visible_catalog', models.BooleanField(default=False, help_text='Whether the instrument is visible for cataloging', verbose_name='instrument is visible in the catalog')),
                ('facility', models.ForeignKey(help_text='The facility the instrument is at (e.g. "SNS")', on_delete=django.db.models.deletion.CASCADE, related_name='instruments', to='catalog.Facility', verbose_name="instrument's facility")),
            ],
            options={
                'ordering': ('beamline',),
            },
        ),
    ]
