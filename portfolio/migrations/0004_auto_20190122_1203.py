# Generated by Django 2.1.5 on 2019-01-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='person',
            name='fone',
            field=models.CharField(default='', max_length=250),
        ),
    ]
