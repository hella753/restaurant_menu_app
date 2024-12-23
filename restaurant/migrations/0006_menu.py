# Generated by Django 5.1.2 on 2024-11-13 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_ingredient_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ManyToManyField(blank=True, null=True, related_name='menus', to='restaurant.dish', verbose_name='კერძი')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant', verbose_name='რესტორანი')),
            ],
        ),
    ]
