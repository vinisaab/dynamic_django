# Generated by Django 3.1.1 on 2020-09-07 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0003_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='page',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='creator.page'),
            preserve_default=False,
        ),
    ]
