from django.db import models

# Create your models here.

class Education(models.Model):

    EDUCATION_TYPES = [('10th', 'Secondary Education (10th)'),('12th', 'Intermediate (12th)'),('degree', 'Bachelor Degree'),]

    education_type = models.CharField(max_length=20,choices=EDUCATION_TYPES)

    institution_name = models.CharField(max_length=200)
    board_or_university = models.CharField(max_length=200)

    year_of_passing = models.CharField(max_length=10)
    percentage = models.CharField(max_length=10, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    # 📄 Marksheet upload (PDF/Image)
    marksheet = models.FileField(upload_to='education/marksheets/',help_text="Upload PDF or image of marksheet")

    # 🏫 School/College Image
    institution_image = models.ImageField(upload_to='education/images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_education_type_display()} - {self.institution_name}"

    class Meta:
        ordering = ['-year_of_passing']
        verbose_name = "Education"
        verbose_name_plural = "Education Details"