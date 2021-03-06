# Generated by Django 3.0 on 2019-12-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('ig_username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('county', models.CharField(choices=[('bungoma', 'Bungoma'), ('busia', 'Busia'), ('kakamega', 'Kakamega'), ('kisumu', 'Kisumu'), ('mombasa', 'Mombasa'), ('nairobi', 'Nairobi'), ('nakuru', 'Nakuru')], max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
