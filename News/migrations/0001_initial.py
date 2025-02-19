# Generated by Django 4.2 on 2024-02-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProsecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ar', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('article_ar', models.TextField()),
                ('article_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AttorneyGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('article_ar', models.TextField()),
                ('article_en', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('start_date', models.DateField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ar', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('article_ar', models.TextField()),
                ('article_en', models.TextField()),
                ('date', models.DateField(default=None)),
                ('image', models.ManyToManyField(blank=True, to='News.image')),
                ('video', models.ManyToManyField(blank=True, to='News.video')),
            ],
        ),
    ]
