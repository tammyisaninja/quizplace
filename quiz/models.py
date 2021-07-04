"""Quiz listing and quiz detail pages"""
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks


class QuizListingPage(Page):
    """Listing page lists all the Quizes that are here"""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        context["quizzes"] = QuizDetailPage.objects.live().public()
        return context

class QuizDetailPage(Page):
    """Quiz Detail Page"""
    template = 'quiz/quiz_detail_page.html'

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    quiz_image = models.ForeignKey(
        "wagtailimages.image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    quiz_desc = RichTextField()

    content = StreamField(
        [
            ("open_ended_question", blocks.OpenEndedQuestion()),
            ("date_question", blocks.DateTimeQuestion()),
            ("multiple_choice_question", blocks.MultipleChoiceQuestion()),
            ("true_false_question", blocks.TrueFalseQuestion()),
            ("fill_in_blanks", blocks.FillInBlanks()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("quiz_desc"),
        ImageChooserPanel("quiz_image"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
