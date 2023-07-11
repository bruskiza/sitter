# Generated by Django 4.2.3 on 2023-07-11 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0002_alter_seat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='user',
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seats.user')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seats.seat')),
            ],
        ),
    ]
