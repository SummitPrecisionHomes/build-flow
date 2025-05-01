import pytest
from django.urls import reverse
from core.models import Project

@pytest.mark.django_db
def test_project_model():
    project = Project.objects.create(
        name="Test Project",
        status="PLANNING",
        start_date="2025-04-01"
    )
    assert project.name == "Test Project"
    assert project.status == "PLANNING"

@pytest.mark.django_db
def test_project_list_view(client):
    url = reverse("project_list")
    response = client.get(url)
    assert response.status_code == 200
    assert "Projects" in response.content.decode()