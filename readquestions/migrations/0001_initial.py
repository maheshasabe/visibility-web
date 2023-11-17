# Generated by Django 4.2.7 on 2023-11-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='readquestions/images')),
                ('url', models.URLField(blank=True)),
                ('company', models.CharField(max_length=200)),
            ],
        ),
    ]
