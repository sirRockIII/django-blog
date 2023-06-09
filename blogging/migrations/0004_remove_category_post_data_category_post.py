# Generated by Django 4.2.1 on 2023-05-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_alter_category_options_remove_category_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.post')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='categories', through='blogging.Data', to='blogging.post'),
        ),
    ]
