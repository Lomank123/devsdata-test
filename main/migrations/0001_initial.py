# Generated by Django 4.0.5 on 2023-02-24 09:27

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
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('start_at', models.DateTimeField(verbose_name='Start at')),
                ('end_at', models.DateTimeField(verbose_name='End at')),
                ('thumbnail', models.ImageField(upload_to='', verbose_name='Thumbnail')),
                ('users', models.ManyToManyField(blank=True, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ReservationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16, verbose_name='Code')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='main.event', verbose_name='Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Reservation code',
                'verbose_name_plural': 'Reservation codes',
                'ordering': ['-id'],
            },
        ),
    ]
