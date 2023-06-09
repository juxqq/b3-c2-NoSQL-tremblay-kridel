# Generated by Django 4.1.7 on 2023-04-05 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='created',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.CreateModel(
            name='AssignationReservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ecole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.ecole')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
