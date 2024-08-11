# Generated by Django 4.2.14 on 2024-08-08 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eveName', models.CharField(max_length=40)),
                ('eveDesc', models.TextField()),
                ('eveDate', models.DateField()),
                ('eveBranch', models.CharField(max_length=10)),
                ('eveYear', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RegEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgEvents.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]