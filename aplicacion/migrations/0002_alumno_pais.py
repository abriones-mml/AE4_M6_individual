# Generated by Django 4.0.4 on 2022-05-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='pais',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
