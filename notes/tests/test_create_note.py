import pytest


pytestmark = [pytest.mark.django_db]


def test_create_note(api):
    response = api.post(
        '/note/create',
    {
        'title': 'New note',
        'description': 'New description'
    },
    expected_status_code=201
    )

    assert response["title"] == "New note"

def test_create_note_unauthenticated(anon):
    anon.post(
        '/note/create',
        {
            'title': 'title',
            'description': 'description'
        },
        expected_status_code=401
    )