from rest_framework.request import Request

from app.errors import ObjectDoesNotExist
from users.models import User
from notes.models import Note
from notes.services.creator import NoteCreator
from notes.services.editor import NoteEditor
from notes.filters import NoteFilter


class NoteToolKit:
    @classmethod
    def create(cls, user: User, title: str, description: str) -> Note:
        return NoteCreator(user=user, title=title, description=description)()

    @classmethod
    def edit(cls, id: int, user: User, title: str, description: str) -> Note:
        return NoteEditor(
            id=id,
            user=user,
            title=title,
            description=description,
        )()

    @classmethod
    def get(cls, request: Request):
        return NoteFilter(request.GET, Note.objects.filter(user=request.user))

    @classmethod
    def delete(cls, id: int, user: User):
        if Note.objects.filter(id=id, user=user).exists():
            Note.objects.get(id=id, user=user).delete()
        else:
            raise ObjectDoesNotExist(f"Note with id - {id} does not exist")

        return True
