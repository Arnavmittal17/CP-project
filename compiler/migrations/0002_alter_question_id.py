# Generated by Django 4.2.7 on 2023-11-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
