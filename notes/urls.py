from django.urls import path

from notes.views import *


urlpatterns = [
    path("create", create_note_api),
    path("<int:id>/edit", edit_note_api),
    path("get", get_notes_api),
    path("<int:id>/delete", delete_note_api)
]
