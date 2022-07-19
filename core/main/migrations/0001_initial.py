# Generated by Django 4.0.6 on 2022-07-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30, verbose_name='Slider name1')),
                ('name2', models.CharField(max_length=30, verbose_name='Slider name2')),
                ('about', models.TextField(verbose_name='Slider name2')),
                ('img', models.ImageField(upload_to='media', verbose_name='Slider image')),
            ],
            options={
                'verbose_name': 'HomeSlider',
                'verbose_name_plural': 'HomeSliders',
            },
        ),
    ]
