# Generated by Django 3.2.7 on 2023-07-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mumbi_django2', '0003_auto_20230726_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='phone',
            field=models.IntegerField(default=1, max_length=15),
        ),
    ]