# Generated by Django 5.0.7 on 2024-07-18 10:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actionApp', '0001_initial'),
        ('mainApp', '0002_alter_product_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'product')},
        ),
    ]
