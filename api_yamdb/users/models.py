from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from users.validators import UsernameRegexValidator


def validate_username(value):
    if value == 'me':
        raise ValidationError('choose another username')


class User(AbstractUser):
    ROLES = (
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Админ'),
    )
    username = models.TextField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[UsernameRegexValidator]
    )
    email = models.EmailField(
        'Почта',
        unique=True,
        max_length=254,
    )
    first_name = models.TextField(
        'Имя',
        blank=True,
        max_length=150,
    )
    last_name = models.TextField(
        'Фамилия',
        blank=True,
        max_length=150,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=max(len(role[1]) for role in ROLES),
        choices=ROLES,
        default=ROLES[0][0]
    )
    confirmation_code = models.CharField(max_length=150, blank=True)

    @property
    def is_admin(self):
        return self.is_superuser or self.role == self.ROLES[2][0]

    @property
    def is_moderator(self):
        return self.role == self.ROLES[1][0]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_user'
            ),
        ]

    def __str__(self):
        return self.username
