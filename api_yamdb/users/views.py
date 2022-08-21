import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .permissions import IsAdmin
from .serializers import (GetTokenSerializer, SignUpSerializer,
                          UserSerializer)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data['username']
    user = get_object_or_404(User, username=username)
    refresh = RefreshToken.for_user(user)
    return Response(
        {'token': str(refresh.access_token)},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def sign_up(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data['username']
    email = request.data['email']
    user = User.objects.filter(username=username, email=email)
    if not user.exists():
        validate = (
            (username == 'me', 'choose another username'),
            (User.objects.filter(username=username).exists(),
             'this username is already being used, try another'),
            (User.objects.filter(email=email).exists(),
             'this e-mail address is already being used, try another')
        )
        for condition, message in validate:
            if condition:
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=username, email=email)
    confirmation_code = secrets.token_hex(16)
    user.update(confirmation_code=confirmation_code)
    send_mail(
        'YaMDB Registration confirmation code',
        f'{confirmation_code}',
        'donotreply@yamdb.db',
        [f'{email}'],
        fail_silently=False,
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)

    @action(detail=False,
            permission_classes=(permissions.IsAuthenticated,),
            methods=['get', 'patch'],
            serializer_class=UserSerializer,
            url_path='me')
    def patch(self, request):
        serializer = self.get_serializer(
            instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=self.request.user.role)
        return Response(serializer.data)
