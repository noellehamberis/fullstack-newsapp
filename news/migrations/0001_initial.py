# Generated by Django 3.1.2 on 2020-10-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image_url', models.URLField(max_length=255, null=True)),
                ('categories', models.CharField(choices=[('Election 2020', 'Election 2020'), ('US News', 'US News'), ('World News', 'Worlds News'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology')], default=None, max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('isTopNews', models.BooleanField(default=False)),
            ],
        ),
    ]
