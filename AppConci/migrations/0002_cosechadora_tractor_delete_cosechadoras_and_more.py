# Generated by Django 4.2 on 2024-09-04 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosechadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='cosechadoras',
        ),
        migrations.DeleteModel(
            name='tractores',
        ),
        migrations.DeleteModel(
            name='ventas',
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default='0000000000', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cuit',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='localidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_completo',
            field=models.CharField(max_length=100),
        ),
    ]