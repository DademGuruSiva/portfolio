from django.db import models

# Create your models here.



from django.db import models

class Skill(models.Model):

    SKILL_TYPES = [('technical', 'Technical Skill'),('soft', 'Soft Skill'),('language', 'Language')]

    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)

    skill_name = models.CharField(max_length=100)

    rating = models.IntegerField(help_text="Enter rating from 1 to 5")

    description = models.TextField(blank=True, null=True)

    # 📄 Certification (like marksheet)
    certification = models.FileField(upload_to='skills/certifications/',   blank=True,null=True,help_text="Upload certificate PDF or image")

    # 🖼 Skill Image (like institution image)
    skill_image = models.ImageField(upload_to='skills/images/',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.skill_name} ({self.skill_type})"