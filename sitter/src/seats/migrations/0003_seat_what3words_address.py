# Generated by Django 4.2.4 on 2023-08-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0002_alter_seat_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='what3words_address',
            field=models.CharField(default='foo.bar.baz', max_length=100),
            preserve_default=False,
        ),
    ]