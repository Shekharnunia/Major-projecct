# Generated by Django 2.1.7 on 2019-03-06 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0008_question_close_question_reason'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-total_votes', '-timestamp'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
    ]