# Generated by Django 5.0.2 on 2024-03-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('room_type', models.CharField(max_length=50)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_rooms', models.IntegerField()),
                ('wifi_available', models.BooleanField(default=True)),
                ('pool_available', models.BooleanField(default=False)),
                ('gym_available', models.BooleanField(default=False)),
                ('Laundry_facilities', models.BooleanField(default=False)),
                ('Parking', models.BooleanField(default=False)),
                ('Restaurant', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
