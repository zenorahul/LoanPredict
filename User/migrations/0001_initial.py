# Generated by Django 5.0.6 on 2024-05-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=90)),
                ('file', models.FileField(upload_to='')),
                ('income', models.IntegerField()),
                ('loanamt', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('loanterm', models.IntegerField()),
            ],
        ),
    ]
