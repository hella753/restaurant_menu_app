# Generated by Django 5.1.2 on 2024-11-13 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_menu_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='restaurant.restaurant', verbose_name='რესტორანი'),
            preserve_default=False,
        ),
    ]
