import pytest


pytestmark = [pytest.mark.django_db]


def test_get_notes(api):
    api.post(
        '/note/create',
    {
        'title': 'New note',
        'description': 'New description'
    },
    expected_status_code=201
    )

    api.post(
        '/note/create',
    {
        'title': 'New note 2',
        'description': 'New description 2'
    },
    expected_status_code=201
    )

    response = api.get(
        '/note/get',
        expected_status_code=200
    )

    assert len(response) == 2

def test_get_note_by_id(api):
    note = api.post(
        '/note/create',
    {
        'title': 'New note',
        'description': 'New description'
    },
    expected_status_code=201
    )

    response = api.get(
        '/note/get',
        headers={
            'id': note['id']
        }
    )
    assert len(response) == 1