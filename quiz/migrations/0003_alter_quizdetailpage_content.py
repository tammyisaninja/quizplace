# Generated by Django 3.2.4 on 2021-07-04 15:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizdetailpage_quiz_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('open_ended_question', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.TextBlock(help_text='Key in your question here', required=True))])), ('date_question', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.TextBlock(help_text='Key in your question here', required=True)), ('date_ans', wagtail.core.blocks.DateTimeBlock(help_text='Answer for the question', required=True))]))]),
        ),
    ]