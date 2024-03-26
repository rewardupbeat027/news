# Generated by Django 5.0.2 on 2024-03-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='files/')),
                ('my_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name:')),
                ('category', models.CharField(max_length=50, verbose_name='Category:')),
                ('full_text', models.TextField(verbose_name='Publication:')),
                ('date', models.DateTimeField(verbose_name='Publication date:')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]