import pytest

from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer as _mixer

from app.test.api_client import DRFClient


pytestmark = [pytest.mark.django_db]

@pytest.fixture
def api():
    return DRFClient()


@pytest.fixture
def anon():
    return DRFClient(anon=True)


@pytest.fixture
def mixer():
    return _mixer

    

@pytest.fixture
def user(mixer):
    return mixer.blend("users.User", username="test@gmail.com", password="password")


@pytest.fixture
def another_user(mixer):
    return mixer.blend("users.User", username="testemail2@gmail.com", password="1234")

@pytest.fixture
def note(mixer, user):
    return mixer.blend("notes.Note", title="Note", description="Note", user=user, id=1)


@pytest.fixture
def anonymous_user(mixer):
    return AnonymousUser()

