# Generated by Django 4.0.2 on 2022-02-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_todolist_todo_pull_todo_todo_pull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='color',
            field=models.CharField(blank=True, max_length=255, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Description'),
        ),
    ]
