# Generated by Django 3.2.8 on 2021-11-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211107_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pain',
            name='labels',
            field=models.ManyToManyField(blank=True, null=True, related_name='pain', to='api.Label'),
        ),
    ]
