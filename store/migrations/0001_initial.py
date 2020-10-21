# Generated by Django 3.0.7 on 2020-10-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Contactno', models.IntegerField()),
                ('Message', models.CharField(max_length=200)),
                ('Attachment', models.ImageField(blank=True, null=True, upload_to='goglestore/')),
            ],
        ),
    ]
