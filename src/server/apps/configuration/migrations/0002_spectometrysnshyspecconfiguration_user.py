# Generated by Django 2.0.2 on 2018-03-06 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='spectometrysnshyspecconfiguration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spectometrysnshyspecconfiguration_users', related_query_name='spectometrysnshyspecconfiguration_user', to=settings.AUTH_USER_MODEL),
        ),
    ]