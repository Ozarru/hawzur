# Generated by Django 3.2.9 on 2021-11-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'video', 'verbose_name_plural': 'videos'},
        ),
        migrations.RemoveField(
            model_name='video',
            name='created',
        ),
        migrations.RemoveField(
            model_name='video',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.RemoveField(
            model_name='video',
            name='snippet',
        ),
        migrations.RemoveField(
            model_name='video',
            name='updated',
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]