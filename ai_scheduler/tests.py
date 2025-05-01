import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_predict_schedule_view(client):
    url = reverse("predict")
    response = client.get(url)
    assert response.status_code == 200
    assert "Predicted Completion" in response.content.decode()