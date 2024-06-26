# Generated by Django 5.0.3 on 2024-04-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.TextField(default='English', help_text="Enter the book's language (e.g. English, Japanese, Chinese, etc.)", max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
