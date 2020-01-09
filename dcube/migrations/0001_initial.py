# Generated by Django 2.2.4 on 2020-01-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('blog', models.TextField(max_length=10000, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
