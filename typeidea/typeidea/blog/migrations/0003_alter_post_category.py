# Generated by Django 5.1.7 on 2025-03-21 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_desc_post_description_rename_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category', verbose_name='分类'),
        ),
    ]
