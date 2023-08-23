from rest_framework.response import Response
from rest_framework.decorators import api_view
from christmas.models import Group, Wish, User
from christmas.serializers import MemberSerializer, GroupSerializer, WishSerializer, CommentSerializer

@api_view(["GET"])
def members_view(request, group_name):
    try:
        group = Group.objects.get(name__iexact=group_name)
        group_serializer = GroupSerializer(instance=group)
        return Response(group_serializer.data)
    except Group.DoesNotExist:
        return Response(status=500)

@api_view(["GET"])
def wishes_view(request, group_name, identifier):
    try:
        group = Group.objects.get(name__iexact=group_name)
        wish = WishSerializer(instance=Wish.objects.all(), many=True)
        return Response(wish.data)
    except Group.DoesNotExist:
        return Response(status=500)

@api_view(["POST"])
def comment_view(request, group_name):
    group = Group.objects.get(name__iexact=group_name)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status_code=500)
    # wish = WishSerializer(instance=Wish.objects.all(), many=True)
    # return Response(wish.data)

@api_view(["DELETE", "POST", "PUT"])
def wish_view(request, identifier = None):
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
    elif request.method == "PUT":
        wish = Wish.objects.get(identifier=identifier)
        serializer = WishSerializer(instance=wish, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=500)

    
