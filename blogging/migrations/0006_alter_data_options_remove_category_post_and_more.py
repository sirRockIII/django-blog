# Generated by Django 4.2.1 on 2023-05-28 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0005_remove_category_post_category_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name_plural': 'DataTest'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', through='blogging.Data', to='blogging.post'),
        ),
    ]
