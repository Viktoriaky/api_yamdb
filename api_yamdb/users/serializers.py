from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .validators import UsernameRegexValidator
from django.core.validators import EmailValidator
from .models import User


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,
                                     validators=[UsernameRegexValidator])
    email = serializers.EmailField(required=True, validators=[EmailValidator])


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,
                                     validators=[UsernameRegexValidator])
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        user = get_object_or_404(User, username=data['username'])
        if not data['confirmation_code'] == user.confirmation_code:
            raise serializers.ValidationError('Wrong confirmation_code')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        model = User
        extra_kwargs = {
            'username': {'validators': [
                UsernameRegexValidator,
                UniqueValidator(queryset=User.objects.all())]},
            'email': {'validators': [
                UniqueValidator(queryset=User.objects.all()), EmailValidator]}
        }
