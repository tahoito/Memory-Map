# Generated by Django 3.2.23 on 2023-12-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spdiary', '0005_auto_20231213_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='relation',
            field=models.ManyToManyField(blank=True, null=True, related_name='_spdiary_diary_relation_+', to='spdiary.Diary', verbose_name='関連'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='tag',
            field=models.ManyToManyField(to='spdiary.Tag', verbose_name='タグ'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='タグ'),
        ),
    ]
