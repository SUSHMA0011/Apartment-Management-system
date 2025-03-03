# Generated by Django 3.2.23 on 2024-07-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FINALApp', '0004_auto_20240722_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
            ],
        ),
    ]
