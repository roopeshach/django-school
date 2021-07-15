# Generated by Django 3.2.5 on 2021-07-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('is_active', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='school_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('room_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.CharField(default=None, max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('salary', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to='teachers/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('caste', models.CharField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateTimeField()),
                ('father_name', models.CharField(max_length=254)),
                ('mother_name', models.CharField(max_length=254)),
                ('contact', models.CharField(max_length=254)),
                ('image', models.ImageField(null=True, upload_to='students/')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.class')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.section')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course_type', models.CharField(max_length=100)),
                ('course_time', models.CharField(max_length=254)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.department')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='class_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
        ),
    ]
