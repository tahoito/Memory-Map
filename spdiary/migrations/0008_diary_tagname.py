# Generated by Django 3.2.23 on 2023-12-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spdiary', '0007_auto_20231216_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='tagname',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='タグ'),
        ),
    ]
