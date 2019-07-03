from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPage

class HomePage(Page):
    def blogs(self):
        blogs = BlogPage.objects.live()
        blogs = blogs.order_by('-first_published_at')[:3]
        return blogs
    
    first_block = models.CharField("Título do primeiro bloco", max_length=255, blank=True)
    first_block_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    first_block_credits = RichTextField("Texto 1", blank=True)
    second_block = models.CharField("Título do segundo bloco", max_length=255, blank=True)
    second_block_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    second_block_text = RichTextField("Créditos da imagem", blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
        [
            InlinePanel('gallery_images', label="Logo do parceiro"),
        ],
        heading="Parceiros",
        classname="collapsible collapsed"
        ),
        MultiFieldPanel(
        [
            FieldPanel('first_block'),
            InlinePanel('topics', label="Tópico"),
            ImageChooserPanel('first_block_image'),
            FieldPanel('first_block_credits'),
        ],
        heading="Primeiro bloco",
        classname="collapsible collapsed"
        ),
        MultiFieldPanel(
        [
            FieldPanel('second_block'),
            FieldPanel('second_block_text'),
            ImageChooserPanel('second_block_image'),
        ],
        heading="Segundo bloco",
        classname="collapsible collapsed"
        ),
    ]

class Topic(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='topics')
    first_block = models.CharField("Título", max_length=255, blank=True)
    first_block_text = RichTextField("Texto", blank=True)

    panels = [
        MultiFieldPanel(
        [
            FieldPanel('first_block'),
            FieldPanel('first_block_text'),
        ],
        heading="Topic",
        classname="collapsible collapsed"
        ),
    ]

class PartnersGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField("Nome do parceiro", blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class StdPage(Page):
    first_block_text = RichTextField("Texto", blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('first_block_text'),
    ]

class CoresPage(Page):
    first_block = models.CharField("Título inicial", max_length=255, blank=True)
    first_block_text = RichTextField("Texto inicial", blank=True)
    second_block = models.CharField("Título", max_length=255, blank=True)
    second_block_text = RichTextField("Texto 1", blank=True)
    second_block_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
        [
            FieldPanel('first_block'),
            FieldPanel('first_block_text'),
        ],
        heading="Texto inicial",
        classname="collapsible collapsed"
        ),
        MultiFieldPanel(
        [
            InlinePanel('cores', label="Núcleo"),
        ],
        heading="Núcleo",
        classname="collapsible collapsed"
        ),
        MultiFieldPanel(
        [
            FieldPanel('second_block'),
            FieldPanel('second_block_text'),
            ImageChooserPanel('second_block_image'),
        ],
        heading="Call to action",
        classname="collapsible collapsed"
        ),
    ]

class Core(Orderable):
    page = ParentalKey(CoresPage, on_delete=models.CASCADE, related_name='cores')
    first_block = models.CharField("Título", max_length=255, blank=True)
    first_block_text = RichTextField("Texto", blank=True)

    panels = [
        MultiFieldPanel(
        [
            FieldPanel('first_block'),
            FieldPanel('first_block_text'),
        ],
        heading="Core",
        classname="collapsible collapsed"
        ),
    ]
