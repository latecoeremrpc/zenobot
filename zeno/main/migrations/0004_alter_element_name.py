# Generated by Django 4.1.2 on 2022-12-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_element_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]