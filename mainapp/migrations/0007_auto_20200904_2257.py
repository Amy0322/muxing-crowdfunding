# Generated by Django 3.0.6 on 2020-09-04 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200829_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Project'),
        ),
    ]
