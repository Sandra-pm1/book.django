# Generated by Django 5.1.2 on 2024-10-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(null=True, upload_to='picture_book'),
        ),
    ]