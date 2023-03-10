import django_filters

from notes.models import Note


class NoteFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Note
        fields = ["title", "id", "created"]
