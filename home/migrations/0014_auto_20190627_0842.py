# Generated by Django 2.1.2 on 2019-06-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190626_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='first_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='fourth_name',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='fourth_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='second_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='third_name',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='third_text',
        ),
        migrations.AlterField(
            model_name='corespage',
            name='first_block',
            field=models.CharField(blank=True, max_length=255, verbose_name='Título inicial'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='first_block',
            field=models.CharField(blank=True, max_length=255, verbose_name='Título do primeiro bloco'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='second_block',
            field=models.CharField(blank=True, max_length=255, verbose_name='Título do segundo bloco'),
        ),
    ]
