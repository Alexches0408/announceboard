# Generated by Django 4.2.2 on 2023-06-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announces', '0003_alter_reply_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='category',
            field=models.CharField(choices=[('tanks', 'Танки'), ('hills', 'Хилы'), ('dd', 'ДД'), ('torg', 'Торговцы'), ('gild', 'Гилдмастеры'), ('quest', 'Квестгиверы'), ('cousn', 'Кузнецы'), ('scin', 'Кожевники'), ('pot', 'Зельевары'), ('magic', 'Мастера заклинаний')], default='tanks', max_length=12),
        ),
    ]
