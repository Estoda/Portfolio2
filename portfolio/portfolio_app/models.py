from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.JSONField()
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="proficiency level from 1 to 100")
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='skill_icons/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Certification(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_link = models.URLField(blank=True, null=True)
    description  = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)# Null if still studying
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.degree} in {self.field_of_study} - {self.institution}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Message from {self.name} - {self.email}"