# Generated by Django 4.1 on 2022-09-29 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='media/post_thumbnail/%Y/%M/%d')),
                ('slug', models.SlugField(max_length=225, unique_for_date='published_date')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=10)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published_date',),
            },
        ),
    ]
