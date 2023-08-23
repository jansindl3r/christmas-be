from rest_framework import serializers
from christmas.models import Group, User, Wish, Comment


class MemberSerializer(serializers.ModelSerializer):
    identifier = serializers.UUIDField(read_only=True)
    class Meta:
        model = User
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    identifier = serializers.UUIDField(read_only=True)
    users = MemberSerializer(many=True)
    class Meta:
        model = Group
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    identifier = serializers.UUIDField(read_only=True)
    author_identifier = serializers.SlugRelatedField(
        source='author',
        queryset=User.objects.all(),
        slug_field="identifier"
    )

    wish_identifier = serializers.SlugRelatedField(
        source='wish',
        queryset=Wish.objects.all(),
        slug_field="identifier"
    )
    class Meta:
        model = Comment
        fields = ("identifier", "content", "author_identifier", "wish_identifier", "created_at")
        read_only_fields = ("created_at", "identifier")

class WishSerializer(serializers.ModelSerializer):
    identifier = serializers.UUIDField(read_only=True)
    user = MemberSerializer(read_only=True)
    user_identifier = serializers.SlugRelatedField(
        source='user',
        queryset=User.objects.all(),
        slug_field="identifier"
    )
    contributor_identifiers = serializers.SlugRelatedField(
        source='contributors',
        queryset=User.objects.all(),
        slug_field="identifier",
        many=True
    )
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Wish
        fields = ("identifier", "user", "user_identifier", "comments", "name", "created_at", "contributor_identifiers", "done")
        read_only_fields = ("created_at",)
        

