# Generated by Django 4.1.5 on 2023-01-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_recharge_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rechargeplans',
            name='recharge_plan',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]