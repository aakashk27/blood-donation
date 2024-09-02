# Generated by Django 4.2.11 on 2024-09-02 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_bloodinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteDonationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('donation_date', models.DateField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.blooddonor')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.donationrequest')),
            ],
        ),
    ]