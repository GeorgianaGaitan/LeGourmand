import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_can_sign_up(client):
    test_username = 'Test_User'
    test_pass = 'Test123!'

    # Folosește clientul pytest-django (fixture)
    response = client.post(reverse('signup'), {
        'username': test_username,
        'password1': test_pass,
        'password2': test_pass,
    })

    # Verifică redirectul spre home
    assert response.status_code == 302
    assert response.url == reverse('home')

    # Verifică dacă userul există în DB
    assert User.objects.filter(username=test_username).exists()
