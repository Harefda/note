from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.utils import get_body_data

from notes.services.toolkit import NoteToolKit
from notes.serializers import NoteSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_note_api(request: Request):
    data = get_body_data(request, ["title", "description"])
    note = NoteToolKit.create(
        title=data["title"], description=data["description"], user=request.user
    )
    serializer = NoteSerializer(instance=note)

    return Response(serializer.data, 201)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_note_api(request: Request, id: int):
    data = get_body_data(request, ["title", "description"])
    note = NoteToolKit.edit(
        id=id, user=request.user, title=data["title"], description=data["description"]
    )

    serializer = NoteSerializer(instance=note)

    return Response(serializer.data, 200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_notes_api(request: Request, format=None):
    notes = NoteToolKit.get(request)
    serializer = NoteSerializer(notes.qs, many=True)

    return Response(serializer.data, 200)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_note_api(request: Request, id: int):
    NoteToolKit.delete(id, request.user)
    return Response(status=204)
