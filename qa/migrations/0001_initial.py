# Generated by Django 2.1.7 on 2019-03-07 04:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('content', models.TextField()),
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_votes', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_answer', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['-is_answer', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question_views', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=80, null=True)),
                ('total_votes', models.IntegerField(default=0)),
                ('favorites', models.IntegerField(default=0)),
                ('has_answer', models.BooleanField(default=False)),
                ('close_question_date', models.DateTimeField(blank=True, null=True)),
                ('close_question_reason', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-total_votes', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.BooleanField(default=True)),
                ('object_id', models.CharField(blank=True, max_length=50, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes_on', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
    ]
