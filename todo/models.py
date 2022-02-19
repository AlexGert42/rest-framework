from django.db import models

class Todolist(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Description')
    color = models.CharField(max_length=255, default='Red', verbose_name='Color')
    priority = models.IntegerField(default=3, verbose_name='Priority')
    time_create = models.TimeField(auto_now=True, verbose_name='Time Create')
    time_update = models.TimeField(auto_now_add=True, verbose_name='Time Update')
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'
        ordering = ['pk']


class Todo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(max_length=1000, verbose_name='Content')
    priority = models.IntegerField(default=3, verbose_name='Priority')
    time_create = models.TimeField(auto_now=True, verbose_name='Time Create')
    time_update = models.TimeField(auto_now_add=True, verbose_name='Time Update')
    todo_pull = models.ForeignKey('Todolist', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Todolist')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['pk']