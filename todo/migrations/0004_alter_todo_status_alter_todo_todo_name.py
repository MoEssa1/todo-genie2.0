

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_user_alter_todo_status_alter_todo_todo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Started', help_text='The status of the task (choices: Not Started, In Progress, Completed)', max_length=20),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_name',
            field=models.CharField(help_text='The name of the task (max 60 characters)', max_length=60),
        ),
    ]
