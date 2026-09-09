from django.db import models

# Create your models here.

from skills.models import Skill   # import Skill model

class Project(models.Model):

    project_title = models.CharField(max_length=200)

    description = models.TextField(help_text="Project Aim / Description",blank=True,null=True)

    # 🛠 Multiple Technologies (checkbox from skills)
    technologies = models.ManyToManyField(Skill,limit_choices_to={'skill_type': 'technical'},help_text="Select technologies used in this project")

    # 🖼 Project Image (like skill image)
    project_image = models.ImageField(upload_to='projects/images/',blank=True,null=True)

    # 🔗 Project URL (for View Project button)
    project_link = models.URLField(blank=True,null=True,help_text="Enter GitHub or Live Project URL")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title