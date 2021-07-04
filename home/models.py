from django.db import models
from django.db.models.fields import related

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel"""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel("carousel_image")
    ]

class HomePage(Page):
    """Home page model"""

    templates = "templates/home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_button_url = models.URLField(default="")
    banner_button_text = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            FieldPanel("banner_button_url"),
            FieldPanel("banner_button_text"),
        ], heading="Banner Options"),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, min_num=1, label="Add Image")
        ], heading="Carousel Images")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"