from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import Project, Skill, Certification, Education, ContactMessage
from .serializers import ProjectSerializer, SkillSerializer, CertificationSerializer, EducationSerializer, ContactMessageSerializer
from .forms import ContactForm
from rest_framework.response import Response
from rest_framework import status

def about(request):
    return render(request, 'portfolio_app/about.html', {
        'year': datetime.now().year,
    })

def skills(request):
    return render(request, 'portfolio_app/skills.html')

def home_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    educations = Education.objects.all()
    return render(request, 'portfolio_app/index.html', {'projects': projects, 'skills': skills, 'educations':educations, 'certifications': certifications})

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/projects.html', {'projects': projects})

def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio_app/skills.html', {'skills': skills})

def education_view(request):
    educations = Education.objects.all()
    return render(request, 'portfolio_app/education.html', {'educations':educations})

def certification_view(request):
    certifications = Certification.objects.all()
    return render(request, 'portfolio_app/certifications.html', {'certifications': certifications})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactMessage(
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            message = form.cleaned_data['message'],
            )
            contact.save()

    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form})

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        data = request.data
        if not (1 <= int(data.get('proficiency', 0)) <= 100):
            return Response(
                {"error": "Proficiency must be between 1 and 100."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'message': 'Skill successfully created!',
                'skill': response.data
            },
            status=status.HTTP_201_CREATED
        )

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

