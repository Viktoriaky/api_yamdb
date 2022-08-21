from django.core.validators import RegexValidator


SlugRegexValidator = RegexValidator(
    r'^[-a-zA-Z0-9_]+$',
    'Только буквы, цифры и _')
