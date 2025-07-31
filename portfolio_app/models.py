# portfolio_app/models.py
from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Technology Name")
    icon_svg_html = models.TextField(help_text="Enter the full HTML for the SVG icon here.", verbose_name="Icon SVG")
    icon_bg_color = models.CharField(max_length=50, default='bg-gray-100', help_text="Background color for the icon (e.g., bg-red-100)", verbose_name="Icon Background Color")
    is_highlighted = models.BooleanField(default=False, help_text="Check this if highlighted.", verbose_name="Is Highlighted?")

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Service Title")
    description = models.TextField(verbose_name="Service Description")
    icon_svg_html = models.TextField(help_text="Enter the full HTML for the SVG icon here.", verbose_name="Icon SVG")
    icon_bg_color = models.CharField(max_length=50, default='bg-gray-100', help_text="Background color for the icon (e.g., bg-teal-100)", verbose_name="Icon Background Color")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Title (e.g., Project Alpha)")
    subtitle = models.CharField(max_length=200, verbose_name="Project Subtitle (e.g., Interactive Dashboards)")
    description = models.TextField(verbose_name="Project Description")
    card_color_class = models.CharField(max_length=50, default='bg-gray-300', help_text="Tailwind CSS class for the card background (e.g., bg-blue-200, bg-teal-500).", verbose_name="Card Color Class")
    project_link = models.URLField(max_length=200, blank=True, null=True, help_text="Live or source code link for the project.", verbose_name="Project Link")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Time")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title