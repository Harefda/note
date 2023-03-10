from typing import Optional

from users.models import User
from notes.models import Note
from app.errors import ValidationError


class NoteCreator:
    def __init__(self, title: str, description: str, user: User):
        self.title = title
        self.description = description
        self.user = user

    def __call__(self) -> Optional[Note]:
        if self.allowed_to_create():
            note = self.create_note()

        return note

    def create_note(self) -> Note:
        return Note.objects.create(
            user=self.user, title=self.title, description=self.description
        )

    def allowed_to_create(self):
        if len(self.description) > 10000:
            raise ValidationError(
                "Description is too long. Please, make it less than 10000 symbols"
            )

        if len(self.title) > 65:
            raise ValidationError(
                "Title is too long. Please, make it less than 65 symbols"
            )

        return True
