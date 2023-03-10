from typing import Optional

from app.errors import ValidationError, ObjectAlreadyExists
from users.models import User
from notes.models import Note


class NoteEditor:
    def __init__(self, id: int, user: User, title: str, description: str):
        self.id = id
        self.user = user
        self.title = title
        self.description = description

    def __call__(self) -> Optional[Note]:
        if self.allowed_to_edit():
            note = self.edit()
        return note

    def edit(self) -> Note:
        note = Note.objects.get(id=self.id)
        note.title = self.title
        note.description = self.description
        note.save()
        return note

    def allowed_to_edit(self):
        if not Note.objects.filter(id=self.id, user=self.user).exists():
            raise ObjectAlreadyExists(f"Note with id - {self.id} does not exists")

        if len(self.description) > 10000:
            raise ValidationError(
                "Description is too long. Please, make it less than 10000 symbols"
            )

        if len(self.title) > 65:
            raise ValidationError(
                "Title is too long. Please, make it less than 65 symbols"
            )

        return True
