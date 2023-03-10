import pytest


pytestmark = [pytest.mark.django_db]


def test_delete_note(api):
    note = api.post(
        '/note/create',
        {
            'title': 'title',
            'description': 'description'
        },
        expected_status_code=201
    )

    api.delete(
        f'/note/{note["id"]}/delete',
        expected_status_code=204,
        empty_content=True
    )

def test_delete_note_does_not_exist(api):
    api.delete(
        '/note/123442132314/delete',
        expected_status_code=400,
    )