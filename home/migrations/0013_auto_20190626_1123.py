# Generated by Django 2.1.2 on 2019-06-26 14:23

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190626_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('first_block', models.CharField(blank=True, max_length=255, verbose_name='Título')),
                ('first_block_text', wagtail.core.fields.RichTextField(blank=True, verbose_name='Texto')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='cores', to='home.CoresPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='topic',
            name='first_block',
            field=models.CharField(blank=True, max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='first_block_text',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='home.HomePage'),
        ),
    ]
