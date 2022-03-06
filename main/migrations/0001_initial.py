# Generated by Django 4.0 on 2022-03-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomi', models.CharField(blank=True, max_length=100, null=True)),
                ('Title', models.CharField(blank=True, max_length=150, null=True)),
                ('Narxi', models.FloatField()),
                ('Tavsif', models.TextField(blank=True, null=True)),
                ('Rasm', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
