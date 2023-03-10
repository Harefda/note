import pytest


pytestmark = [pytest.mark.django_db]


def test_edit_note_does_not_exists(api, note):
    api.put(
        '/note/1/edit',
        {
            'title': 'title',
            'description': 'description'
        },
        expected_status_code=400
    )

def test_edit_note(api):
    note = api.post(
        '/note/create',
        {
            'title': 'title',
            'description': 'description'
        },
        expected_status_code=201
    )

    response = api.put(
        f'/note/{note["id"]}/edit',
        {
            'title': 'new title',
            'description': 'new_description'
        },
        expected_status_code=200
    )
    assert response["title"] == 'new title'
