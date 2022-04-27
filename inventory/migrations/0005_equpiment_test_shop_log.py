# Generated by Django 3.2.5 on 2022-04-04 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_deployment_remove_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_in', models.DateTimeField()),
                ('checked_out', models.DateTimeField(blank=True, null=True)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Equpiment_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(choices=[('B', 'Bench'), ('F', 'Field')], default='B', max_length=1)),
                ('result', models.CharField(choices=[('P', 'Pass'), ('F', 'Fail'), ('O', 'Other')], max_length=1)),
                ('test_date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.equipment')),
            ],
        ),
    ]