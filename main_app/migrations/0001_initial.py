# Generated by Django 4.1 on 2022-08-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('rooms_baths', models.CharField(max_length=10)),
                ('sqft', models.IntegerField()),
                ('gas_stove', models.BooleanField()),
                ('notes', models.CharField(max_length=300)),
                ('allows_dogs', models.BooleanField()),
            ],
        ),
    ]
