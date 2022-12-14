# Generated by Django 4.1.3 on 2022-12-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('short_address', models.CharField(max_length=120)),
                ('no', models.PositiveBigIntegerField()),
                ('unit', models.PositiveBigIntegerField()),
                ('zip_code', models.PositiveBigIntegerField()),
            ],
        ),
    ]
