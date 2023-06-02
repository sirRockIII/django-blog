# Generated by Django 4.2.1 on 2023-05-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0006_alter_data_options_remove_category_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
       ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='blogging.post'),
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
