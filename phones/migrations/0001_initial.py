# Generated by Django 4.2 on 2024-11-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=50, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('screen_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
                ('country_made', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.country')),
            ],
        ),
    ]