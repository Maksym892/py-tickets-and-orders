from django.contrib.auth import get_user_model
from typing import Any


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> Any:
    user_model = get_user_model()
    kwargs = {}
    if email:
        kwargs["email"] = email
    if first_name:
        kwargs["first_name"] = first_name
    if last_name:
        kwargs["last_name"] = last_name
    return user_model.objects.create_user(
        username=username,
        password=password,
        **kwargs
    )
