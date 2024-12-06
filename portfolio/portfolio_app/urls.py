from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'contact-messages', views.ContactMessageViewSet)

urlpatterns = [
    path('', views.about, name='home'),
    path('projects/',views.projects_view, name='projects'),
    path('skills/',views.skills_view, name='skills'),
    path('education/',views.education_view, name='education'),
    path('certifications/',views.certification_view, name='certifications'),
    path('contacts/',views.contact_view, name='contact'),
    path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)