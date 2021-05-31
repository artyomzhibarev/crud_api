from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'create_at', 'status', 'author')
        # read_only_fields = ('create_at', 'author')

    # title = models.CharField(max_length=100)
    # text = models.TextField(default='', blank=True)
    # create_at = models.DateTimeField(auto_now=True)
    # status = models.PositiveIntegerField(choices=STATUS, default=0)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
