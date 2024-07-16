# Generated by Django 5.0.6 on 2024-07-12 04:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gyms', '0002_personalinfo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('timeslot_id', models.AutoField(primary_key=True, serialize=False)),
                ('slot', models.CharField(choices=[('18:00 - 18:30', '18:00 - 18:30'), ('18:30 - 19:00', '18:30 - 19:00'), ('19:00 - 19:30', '19:00 - 19:30'), ('19:30 - 20:00', '19:30 - 20:00'), ('20:00 - 20:30', '20:00 - 20:30'), ('20:30 - 21:00', '20:30 - 21:00')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('equipment_name', models.CharField(max_length=50)),
                ('equipment_type', models.CharField(max_length=50)),
                ('equipment_description', models.TextField(blank=True, null=True)),
                ('equipment_image', models.ImageField(blank=True, null=True, upload_to='equipment_images/')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gyms.gym')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentReservation',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('res_start_time', models.DateTimeField(null=True)),
                ('res_end_time', models.DateTimeField(null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.timeslot')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentInUse',
            fields=[
                ('use_equip_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('res', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.equipmentreservation')),
            ],
        ),
    ]
