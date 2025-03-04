# Generated by Django 5.1.6 on 2025-02-19 13:04

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_alter_announcementpage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(help_text='Title of the individual announcement', max_length=255)),
                ('content', models.TextField(help_text='Content of the announcement')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_items', to='departments.announcementpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
