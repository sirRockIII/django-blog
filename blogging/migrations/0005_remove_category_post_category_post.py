# Generated by Django 4.2.1 on 2023-05-28 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_remove_category_post_data_category_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='blogging.post'),
            preserve_default=False,
        ),
    ]
