from django.core.validators import RegexValidator


UsernameRegexValidator = RegexValidator(
    r'^[\w.@+-]+$',
    'Только буквы, цифры и @.+-_')
