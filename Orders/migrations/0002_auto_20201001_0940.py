# Generated by Django 3.1.1 on 2020-10-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Username'),
        ),
    ]