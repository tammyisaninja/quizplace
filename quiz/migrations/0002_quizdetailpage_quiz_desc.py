# Generated by Django 3.2.4 on 2021-06-29 17:15

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizdetailpage',
            name='quiz_desc',
            field=wagtail.core.fields.RichTextField(default='Description of Quiz'),
            preserve_default=False,
        ),
    ]
