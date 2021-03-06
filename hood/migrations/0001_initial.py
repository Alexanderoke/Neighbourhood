# Generated by Django 4.0.3 on 2022-03-22 07:40

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
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NeighbourhoodName', models.CharField(max_length=100)),
                ('NeighbourHoodLocation', models.CharField(max_length=200)),
                ('OccupantsCount', models.IntegerField()),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bussiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_name', models.CharField(max_length=200)),
                ('Business_email', models.EmailField(max_length=200)),
                ('NeighbourHood_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hood.neighbourhood')),
            ],
        ),
    ]
