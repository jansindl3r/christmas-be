from rest_framework.response import Response
from rest_framework.decorators import api_view
from christmas.models import Group, Wish, User
from christmas.serializers import MemberSerializer, GroupSerializer, WishSerializer, CommentSerializer

@api_view(["GET"])
def members_view(request):
    group = GroupSerializer(instance=Group.objects.first())
    return Response(group.data)

@api_view(["GET"])
def wishes_view(request, identifier):
    wish = WishSerializer(instance=Wish.objects.all(), many=True)
    return Response(wish.data)

@api_view(["POST"])
def comment_view(request):
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status_code=500)
    # wish = WishSerializer(instance=Wish.objects.all(), many=True)
    # return Response(wish.data)

@api_view(["DELETE", "POST"])
def wish_view(request, identifier = None):
    print(request.data)
    print(request.method)
    if request.method == "DELETE":
        Wish.objects.get(identifier=identifier).delete()
        return Response({})
    elif request.method == "POST":
        serializer = WishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)
