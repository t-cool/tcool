# Generated by Django 2.1.5 on 2019-02-06 12:08

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('grammarcheck', '0002_auto_20190203_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammarcheckhistory',
            name='_picked_obj',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]
