# Generated by Django 4.2 on 2023-10-14 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_es_admin_user_es_usuario_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
