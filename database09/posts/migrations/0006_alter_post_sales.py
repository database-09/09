# Generated by Django 4.2.7 on 2023-12-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_merge_20231202_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sales',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='가격'),
        ),
    ]
