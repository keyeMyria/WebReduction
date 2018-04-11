# Generated by Django 2.0.2 on 2018-04-11 15:17

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import server.apps.reduction.models.abstract


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_remote_submission', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReductionBioSANS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script_execution_path', models.CharField(max_length=256)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.         If the script was generated already just shows it!')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reductionbiosans_instruments', related_query_name='reductionbiosans_instrument', to='catalog.Instrument')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductionbiosans_job', related_query_name='reductionbiosans_job', to='django_remote_submission.Job')),
                ('script_interpreter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductionbiosans_interpreters', related_query_name='reductionbiosans_interpreter', to='django_remote_submission.Interpreter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reductionbiosans_users', related_query_name='reductionbiosans_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.reduction.models.abstract.ModelMixin),
        ),
        migrations.CreateModel(
            name='ReductionGPSANS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script_execution_path', models.CharField(max_length=256)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.         If the script was generated already just shows it!')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reductiongpsans_instruments', related_query_name='reductiongpsans_instrument', to='catalog.Instrument')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductiongpsans_job', related_query_name='reductiongpsans_job', to='django_remote_submission.Job')),
                ('script_interpreter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductiongpsans_interpreters', related_query_name='reductiongpsans_interpreter', to='django_remote_submission.Interpreter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reductiongpsans_users', related_query_name='reductiongpsans_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.reduction.models.abstract.ModelMixin),
        ),
        migrations.CreateModel(
            name='ReductionHYSPEC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script_execution_path', models.CharField(max_length=256)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.         If the script was generated already just shows it!')),
                ('field3', models.CharField(blank=True, help_text='Help for the field.', max_length=128, verbose_name='Human description 3')),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='configuration.ConfigurationHYSPEC')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reductionhyspec_instruments', related_query_name='reductionhyspec_instrument', to='catalog.Instrument')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductionhyspec_job', related_query_name='reductionhyspec_job', to='django_remote_submission.Job')),
                ('script_interpreter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reductionhyspec_interpreters', related_query_name='reductionhyspec_interpreter', to='django_remote_submission.Interpreter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reductionhyspec_users', related_query_name='reductionhyspec_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.reduction.models.abstract.ModelMixin),
        ),
        migrations.CreateModel(
            name='RegionBioSANS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('empty_beam_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Empty Beam Transmission')),
                ('beam_center_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Beam Center')),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('entries', django.contrib.postgres.fields.jsonb.JSONField()),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='configuration.ConfigurationBioSANS')),
                ('reduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='reduction.ReductionBioSANS')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, server.apps.reduction.models.abstract.ModelMixin),
        ),
        migrations.CreateModel(
            name='RegionGPSANS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('empty_beam_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Empty Beam Transmission')),
                ('beam_center_run', models.CharField(blank=True, help_text='Use run number or file path. If empty, uses that of the Configuration.', max_length=128, verbose_name='Beam Center')),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('entries', django.contrib.postgres.fields.jsonb.JSONField()),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='configuration.ConfigurationGPSANS')),
                ('reduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='reduction.ReductionGPSANS')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, server.apps.reduction.models.abstract.ModelMixin),
        ),
        migrations.CreateModel(
            name='RegionHYSPEC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('field1', models.CharField(blank=True, help_text='Help fr the field.', max_length=128, verbose_name='Human description 1')),
                ('field2', models.CharField(blank=True, help_text='Help fr the field.', max_length=128, verbose_name='Human description 2')),
                ('reduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='reduction.ReductionHYSPEC')),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.reduction.models.abstract.ModelMixin),
        ),
    ]
