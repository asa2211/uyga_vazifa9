# Generated by Django 4.2.4 on 2023-08-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subjectmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='added_at',
            field=models.DateTimeField(default=''),
        ),
    ]