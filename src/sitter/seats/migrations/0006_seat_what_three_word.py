# Generated by Django 4.2.3 on 2023-07-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0005_remove_allocation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='what_three_word',
            field=models.CharField(default='foo.bar.baz', max_length=100),
            preserve_default=False,
        ),
    ]