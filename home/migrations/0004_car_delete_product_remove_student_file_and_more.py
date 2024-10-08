# Generated by Django 5.0.7 on 2024-08-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=500)),
                ('speed', models.ImageField(default=50, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='images',
        ),
    ]
