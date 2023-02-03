# Generated by Django 4.1.5 on 2023-02-03 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='done',
            field=models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], max_length=5),
        ),
    ]
