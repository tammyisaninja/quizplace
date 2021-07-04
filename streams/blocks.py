"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text Only"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)"""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=400)),
                ("text", blocks.CharBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(
                    required=False,
                    help_text="If button page above is selected, that will be used first."
                )),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"

class OpenEndedQuestion(blocks.StructBlock):
    """Question and space for input"""

    question = blocks.TextBlock(required=True, help_text="Key in your question here")
    ans = blocks.TextBlock(required=True, help_text="Key in your answer here")

    class Meta:
        template = "streams/open_ended_question.html"
        icon = "question"
        label = "Open Ended Question"


class DateTimeQuestion(blocks.StructBlock):
    """Questions that require a date for an answer"""

    question = blocks.TextBlock(required=True, help_text="Key in your question here")
    date_ans = blocks.DateTimeBlock(required=True, help_text="Answer for the question")

    class Meta:
        template = "streams/date_question.html"
        icon = "placeholder"
        label = "Date Question"

class MultipleChoiceQuestion(blocks.StructBlock):
    """Question with multiple choice answers"""

    question = blocks.TextBlock(required=True, help_text="Key in your question here")
    ans = blocks.IntegerBlock(required=True, help_text="Key in the option number for the ans here")
    options = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("option_text", blocks.TextBlock(required=True, help_text="Option for the question"))
            ])
    )

    class Meta:
        template = "streams/multiple_choice_question.html"
        icon = "placeholder"
        label = "Multiple Choice Question"

class TrueFalseQuestion(blocks.StructBlock):
    """True False question with only 2 options for the answer"""

    question = blocks.TextBlock(required=True, help_text="Key in your question here")
    ans = blocks.ChoiceBlock(choices=[
            ('True', 'True'),
            ('False', 'False'),
        ],
        required=True,
        help_text="Key in the ans here"
    )

    class Meta:
        template = "streams/true_false_question.html"
        icon = "placeholder"
        label = "True False Question"

class FillInBlanks(blocks.StructBlock):
    """Question with multiple choice answers"""

    first_part = blocks.TextBlock(required=True, help_text="Key in first part of question before blank here")
    second_part = blocks.TextBlock(required=True, help_text="Key in second part of question after blank here")
    ans = blocks.TextBlock(required=True, help_text="Key in your answer here")
    options = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("option_text", blocks.TextBlock(required=True, help_text="Option for the question"))
            ])
    )


    class Meta:
        template = "streams/fill_in_blanks.html"
        icon = "placeholder"
        label = "Fill in the Blank Question"