# Generated by Django 4.1.2 on 2022-12-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_element_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='link',
            field=models.CharField(max_length=2000),
        ),
    ]