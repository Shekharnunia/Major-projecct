# Generated by Django 2.1.5 on 2019-02-04 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]
