# Generated by Django 4.0.2 on 2022-02-19 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todolist_todo_pull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='todo_pull',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todo', verbose_name='Todo'),
        ),
    ]
